import argparse
import csv
import json
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


DISABLED_RULES = "UPPERCASE_SENTENCE_START"
SPELLCHECK_RULE_IDS = {
    "MORFOLOGIK_RULE_EN_US",
    "GERMAN_SPELLER_RULE",
    "CAFE_DIACRITIC",
}


@dataclass
class Entry:
    file_name: str
    row_number: int
    column_name: str
    text: str


def read_entries(csv_dir):
    english_entries = []
    german_entries = []

    for path in sorted(csv_dir.glob("dict_*.csv")):
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or len(reader.fieldnames) < 2:
                continue

            prompt_column, answer_column = reader.fieldnames[:2]

            for row_number, row in enumerate(reader, start=2):
                prompt = (row.get(prompt_column) or "").strip()
                answer = (row.get(answer_column) or "").strip()

                if prompt:
                    english_entries.append(Entry(path.name, row_number, prompt_column, prompt))
                if answer:
                    german_entries.append(Entry(path.name, row_number, answer_column, answer))

    return english_entries, german_entries


def write_text_file(entries, path):
    offsets = []
    position = 0
    lines = []

    for entry in entries:
        line = entry.text
        offsets.append((position, position + len(line), entry))
        lines.append(line)
        position += len(line) + 1

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return offsets


def entry_for_offset(offsets, offset):
    for start, end, entry in offsets:
        if start <= offset <= end:
            return entry
    return None


def run_languagetool(language, entries, temp_dir, include_all):
    text_path = temp_dir / f"{language}.txt"
    offsets = write_text_file(entries, text_path)

    command = [
        "languagetool",
        "--json",
        "--language",
        language,
        "--disable",
        DISABLED_RULES,
        str(text_path),
    ]

    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
    )

    if completed.returncode not in {0, 1}:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())

    data = json.loads(completed.stdout)
    findings = []

    for match in data.get("matches", []):
        rule = match.get("rule", {})
        rule_id = rule.get("id", "")

        if not include_all:
            is_spellcheck_finding = rule_id in SPELLCHECK_RULE_IDS
            if not is_spellcheck_finding:
                continue

        entry = entry_for_offset(offsets, match.get("offset", 0))
        if entry is None:
            continue

        replacements = match.get("replacements", [])
        suggestions = ", ".join(item["value"] for item in replacements[:5])
        category = rule.get("category", {})

        findings.append({
            "language": language,
            "file_name": entry.file_name,
            "row_number": entry.row_number,
            "column_name": entry.column_name,
            "text": entry.text,
            "message": match.get("message", ""),
            "rule_id": rule_id,
            "category": category.get("name", ""),
            "suggestions": suggestions,
        })

    return findings


def write_report(report_path, findings):
    report_path.parent.mkdir(exist_ok=True)

    lines = [
        "# LanguageTool Dictionary Check",
        "",
        "This is a manual developer report. It can contain false positives,",
        "especially because dictionary entries are short phrases, not full sentences.",
        "",
        f"Findings: {len(findings)}",
        "",
    ]

    if findings:
        lines.extend([
            "| Language | File | Row | Column | Text | Message | Rule | Suggestions |",
            "| --- | --- | ---: | --- | --- | --- | --- | --- |",
        ])

        for finding in findings:
            lines.append(
                "| {language} | {file_name} | {row_number} | {column_name} | {text} | {message} | {rule_id} | {suggestions} |".format(
                    **{key: str(value).replace("|", "\\|") for key, value in finding.items()}
                )
            )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Run a manual LanguageTool check over dictionary CSV files."
    )
    parser.add_argument("--csv-dir", default="csv-files", type=Path)
    parser.add_argument(
        "--report",
        default=Path("validation_reports/languagetool_report.md"),
        type=Path,
    )
    parser.add_argument(
        "--all-rules",
        action="store_true",
        help="Include grammar/style findings too. By default only typo-like findings are reported.",
    )
    args = parser.parse_args()

    if shutil.which("languagetool") is None:
        raise SystemExit("LanguageTool CLI was not found on PATH.")

    english_entries, german_entries = read_entries(args.csv_dir)

    with tempfile.TemporaryDirectory() as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        findings = []
        findings.extend(run_languagetool("en-US", english_entries, temp_dir, args.all_rules))
        findings.extend(run_languagetool("de-DE", german_entries, temp_dir, args.all_rules))

    write_report(args.report, findings)

    print(f"Checked English entries: {len(english_entries)}")
    print(f"Checked German entries:  {len(german_entries)}")
    print(f"Findings: {len(findings)}")
    print(f"Report: {args.report}")


if __name__ == "__main__":
    main()
