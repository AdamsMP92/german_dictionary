import csv
import random
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DICTIONARY_DIR = BASE_DIR / "csv-files"
TRAINING_LOG_DIR = BASE_DIR / "training_log"


def list_dictionaries():
    return sorted(DICTIONARY_DIR.glob("*.csv"))


def load_dictionary(path):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        if len(fieldnames) < 2:
            raise ValueError("Dictionary file muss mindestens zwei Spalten haben.")
        prompt_column, answer_column = fieldnames[:2]
        rows = [
            {
                "Prompt": (row.get(prompt_column) or "").strip(),
                "ExpectedAnswer": (row.get(answer_column) or "").strip(),
            }
            for row in reader
        ]
    rows = [row for row in rows if row["Prompt"] and row["ExpectedAnswer"]]
    if not rows:
        raise ValueError(f"Dictionary file ist leer: {path}")
    return rows, prompt_column, answer_column


def normalize(value):
    return " ".join(str(value).strip().lower().split())


def ask_yes_no(prompt, default=False):
    suffix = "J/n" if default else "j/N"
    answer = input(f"{prompt} [{suffix}] ").strip().lower()
    if not answer:
        return default
    return answer in {"j", "ja", "y", "yes"}


def ask_number(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(f"{prompt} [{minimum}-{maximum}] ").strip())
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Bitte eine Zahl zwischen {minimum} und {maximum} eingeben.")


def choose_dictionary():
    files = list_dictionaries()
    if not files:
        raise FileNotFoundError(f"Keine CSV-Dateien gefunden in {DICTIONARY_DIR}.")

    print("Verfuegbare Dictionary-Dateien:")
    for index, path in enumerate(files, start=1):
        print(f"{index}. {path.name}")
    print()

    raw = input("Nummer oder Dateiname eingeben: ").strip()
    if raw.isdigit():
        index = int(raw) - 1
        if not 0 <= index < len(files):
            raise ValueError("Ungueltige Dictionary-Nummer.")
        return files[index]

    path = DICTIONARY_DIR / raw
    if path.exists():
        return path
    raise FileNotFoundError(f"Dictionary file nicht gefunden: {raw}")


def make_log_file(dictionary_path):
    TRAINING_LOG_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return TRAINING_LOG_DIR / f"iphone_vocab_test_log_{timestamp}_{dictionary_path.stem}.csv"


def write_log(path, results):
    fieldnames = [
        "answer_time",
        "dictionary_file",
        "prompt",
        "expected_answer",
        "given_answer",
        "correct",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    dictionary_path = choose_dictionary()
    rows, prompt_column, answer_column = load_dictionary(dictionary_path)

    if ask_yes_no("Abfragerichtung umkehren?", False):
        prompt_column, answer_column = answer_column, prompt_column
        rows = [
            {"Prompt": row["ExpectedAnswer"], "ExpectedAnswer": row["Prompt"]}
            for row in rows
        ]

    n_words = ask_number("Wie viele Vokabeln sollen abgefragt werden?", 1, len(rows))
    random.shuffle(rows)
    rows = rows[:n_words]

    print("\nVokabeltest gestartet. Gib 'q' ein, um abzubrechen.\n")
    results = []
    correct = 0

    for row in rows:
        print(f"{prompt_column}: {row['Prompt']}")
        answer = input(f"{answer_column}: ").strip()
        if normalize(answer) == "q":
            break

        is_correct = normalize(answer) == normalize(row["ExpectedAnswer"])
        correct += int(is_correct)
        if is_correct:
            print("Richtig.\n")
        else:
            print(f"Falsch. Richtig waere: {row['ExpectedAnswer']}\n")

        results.append(
            {
                "answer_time": datetime.now().isoformat(timespec="seconds"),
                "dictionary_file": str(dictionary_path),
                "prompt": row["Prompt"],
                "expected_answer": row["ExpectedAnswer"],
                "given_answer": answer,
                "correct": str(is_correct),
            }
        )

    log_file = make_log_file(dictionary_path)
    write_log(log_file, results)
    total = len(results)
    wrong = total - correct
    score = 100 * correct / total if total else 0

    print("Auswertung:")
    print(f"Abgefragt: {total}")
    print(f"Richtig:   {correct}")
    print(f"Falsch:    {wrong}")
    print(f"Quote:     {score:.1f}%")
    print(f"Logfile:   {log_file}")


if __name__ == "__main__":
    main()
