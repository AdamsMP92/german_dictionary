import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path


FILENAME_PATTERN = re.compile(r"^dict_(Nomen|Verben|Adjektive)_(.+)\.csv$")
GERMAN_ARTICLES = ("der ", "die ", "das ")


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def add_issue(issues, severity, path, message):
    issues.append((severity, path, message))


def validate_file(path, generators_dir, min_counts, issues):
    match = FILENAME_PATTERN.match(path.name)
    if not match:
        add_issue(issues, "ERROR", path, "filename should match dict_<Wortart>_<Thema>.csv")
        return 0

    word_type = match.group(1)
    generator_path = generators_dir / path.name.replace(".csv", ".py")
    if not generator_path.exists():
        add_issue(issues, "ERROR", path, f"missing generator {generator_path}")

    fieldnames, rows = read_rows(path)
    if len(fieldnames) < 2:
        add_issue(issues, "ERROR", path, "CSV needs at least two columns")
        return 0

    prompt_column, answer_column = fieldnames[:2]
    if prompt_column != "English" or answer_column != "German":
        add_issue(
            issues,
            "WARN",
            path,
            f"first columns are {prompt_column!r}, {answer_column!r}; test.py supports this, but dictionary lists usually use English,German",
        )

    min_count = min_counts[word_type]
    if len(rows) < min_count:
        add_issue(issues, "ERROR", path, f"only {len(rows)} rows; expected at least {min_count}")

    seen_prompts = defaultdict(list)
    seen_pairs = defaultdict(list)
    seen_answers = defaultdict(list)

    for row_number, row in enumerate(rows, start=2):
        prompt = (row.get(prompt_column) or "").strip()
        answer = (row.get(answer_column) or "").strip()

        if not prompt or not answer:
            add_issue(issues, "ERROR", path, f"row {row_number} has an empty prompt or answer")
            continue

        seen_prompts[prompt.lower()].append(row_number)
        seen_pairs[(prompt.lower(), answer.lower())].append(row_number)
        seen_answers[answer.lower()].append(row_number)

        if word_type == "Nomen":
            if not prompt.lower().startswith("the "):
                add_issue(issues, "ERROR", path, f"row {row_number}: noun prompt should start with 'the '")
            if not answer.lower().startswith(GERMAN_ARTICLES):
                add_issue(issues, "ERROR", path, f"row {row_number}: noun answer should start with der/die/das")
        elif word_type == "Verben":
            if not prompt.lower().startswith("to "):
                add_issue(issues, "ERROR", path, f"row {row_number}: verb prompt should start with 'to '")
            if answer.lower().startswith(GERMAN_ARTICLES) and len(answer.split()) <= 2:
                add_issue(issues, "WARN", path, f"row {row_number}: verb answer looks like a noun")
        elif word_type == "Adjektive":
            if prompt.lower().startswith(("the ", "to ")):
                add_issue(issues, "WARN", path, f"row {row_number}: adjective prompt looks like another word type")
            if answer.lower().startswith(GERMAN_ARTICLES):
                add_issue(issues, "WARN", path, f"row {row_number}: adjective answer looks like a noun")

    for prompt, line_numbers in seen_prompts.items():
        if len(line_numbers) > 1:
            add_issue(issues, "ERROR", path, f"duplicate prompt {prompt!r} on rows {line_numbers}")

    for pair, line_numbers in seen_pairs.items():
        if len(line_numbers) > 1:
            add_issue(issues, "ERROR", path, f"duplicate pair {pair!r} on rows {line_numbers}")

    for answer, line_numbers in seen_answers.items():
        if len(line_numbers) > 1:
            add_issue(issues, "WARN", path, f"duplicate answer {answer!r} on rows {line_numbers}")

    return len(rows)


def main():
    parser = argparse.ArgumentParser(description="Validate dictionary CSV files.")
    parser.add_argument("--csv-dir", default="csv-files", type=Path)
    parser.add_argument("--generators-dir", default="generators", type=Path)
    parser.add_argument("--min-nouns", default=20, type=int)
    parser.add_argument("--min-verbs", default=20, type=int)
    parser.add_argument("--min-adjectives", default=20, type=int)
    args = parser.parse_args()

    min_counts = {
        "Nomen": args.min_nouns,
        "Verben": args.min_verbs,
        "Adjektive": args.min_adjectives,
    }

    issues = []
    csv_files = sorted(args.csv_dir.glob("dict_*.csv"))

    if not csv_files:
        print(f"No dictionary CSV files found in {args.csv_dir}.", file=sys.stderr)
        return 1

    total_rows = 0
    rows_by_type = defaultdict(int)
    files_by_type = defaultdict(int)

    for path in csv_files:
        row_count = validate_file(path, args.generators_dir, min_counts, issues)
        total_rows += row_count
        match = FILENAME_PATTERN.match(path.name)
        if match:
            word_type = match.group(1)
            rows_by_type[word_type] += row_count
            files_by_type[word_type] += 1

    print("Dictionary validation summary")
    print(f"Files: {len(csv_files)}")
    print(f"Rows:  {total_rows}")
    for word_type in ("Nomen", "Verben", "Adjektive"):
        print(f"{word_type}: {files_by_type[word_type]} files, {rows_by_type[word_type]} rows")

    errors = [issue for issue in issues if issue[0] == "ERROR"]
    warnings = [issue for issue in issues if issue[0] == "WARN"]

    if issues:
        print()
        for severity, path, message in issues:
            print(f"{severity}: {path}: {message}")

    print()
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
