from datetime import datetime
from pathlib import Path

import pandas as pd


DICTIONARY_DIR = Path("csv-files")
TRAINING_LOG_DIR = Path("training_log")


def list_dictionaries(dictionary_dir=DICTIONARY_DIR):
    return sorted(dictionary_dir.glob("*.csv"))


def resolve_dictionary_path(dictionary_file, dictionary_dir=DICTIONARY_DIR):
    available_dictionaries = list_dictionaries(dictionary_dir)

    if str(dictionary_file).isdigit() and available_dictionaries:
        selected_index = int(dictionary_file) - 1
        if not 0 <= selected_index < len(available_dictionaries):
            raise ValueError("Ungültige Dictionary-Nummer.")
        return available_dictionaries[selected_index]

    dictionary_path = Path(dictionary_file)
    if not dictionary_path.exists():
        dictionary_path = dictionary_dir / str(dictionary_file)

    if not dictionary_path.exists():
        raise FileNotFoundError(f"Dictionary file nicht gefunden: {dictionary_file}")

    return dictionary_path


def load_dictionary(dictionary_path, swap_direction=False):
    df = pd.read_csv(dictionary_path)

    if len(df.columns) < 2:
        raise ValueError("Dictionary file muss mindestens zwei Spalten haben.")

    prompt_column = df.columns[0]
    answer_column = df.columns[1]
    df = df[[prompt_column, answer_column]].rename(
        columns={
            prompt_column: "Prompt",
            answer_column: "ExpectedAnswer",
        }
    )

    if swap_direction:
        prompt_column, answer_column = answer_column, prompt_column
        df = df.rename(
            columns={
                "Prompt": "ExpectedAnswer",
                "ExpectedAnswer": "Prompt",
            }
        )

    if len(df) == 0:
        raise ValueError(f"Dictionary file ist leer: {dictionary_path}")

    return df, prompt_column, answer_column


def normalize_answer(value):
    return str(value).strip().lower()


def make_log_file(dictionary_path, test_start, log_dir=TRAINING_LOG_DIR):
    log_dir.mkdir(exist_ok=True)
    test_start_string = test_start.strftime("%Y-%m-%d_%H-%M-%S_%f")
    stem = Path(dictionary_path).stem
    return log_dir / f"vocab_test_log_{test_start_string}_{stem}.csv"


def save_results(
    results,
    log_file,
    dictionary_path,
    prompt_column,
    answer_column,
    n_available,
    n_words,
    test_start,
):
    log_df = pd.DataFrame(results)

    if len(log_df) == 0:
        return log_df

    n_total = len(log_df)
    n_correct = int(log_df["correct"].sum())
    n_wrong = n_total - n_correct
    score_percent = 100 * n_correct / n_total
    wrong_words = log_df[log_df["correct"] == False]

    log_df.to_csv(log_file, index=False)

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("# Statistik\n")
        f.write(f"# Dictionary file,{dictionary_path}\n")
        f.write(f"# Frage-Spalte,{prompt_column}\n")
        f.write(f"# Antwort-Spalte,{answer_column}\n")
        f.write(f"# Testbeginn,{test_start.isoformat(timespec='seconds')}\n")
        f.write(f"# Verfügbare Vokabeln,{n_available}\n")
        f.write(f"# Gewählte Vokabeln,{n_words}\n")
        f.write(f"# Tatsächlich abgefragt,{n_total}\n")
        f.write(f"# Richtig,{n_correct}\n")
        f.write(f"# Falsch,{n_wrong}\n")
        f.write(f"# Quote,{score_percent:.1f}%\n")

        if len(wrong_words) > 0:
            f.write("\n")
            f.write("# Falsch beantwortete Vokabeln\n")
            f.write("prompt,expected_answer,given_answer\n")

            wrong_words[["prompt", "expected_answer", "given_answer"]].to_csv(
                f,
                index=False,
                header=False,
            )

    return log_df


def run_vocab_test(
    dictionary_path,
    n_words,
    swap_direction=False,
    log_dir=TRAINING_LOG_DIR,
    run_label=None,
):
    df, prompt_column, answer_column = load_dictionary(dictionary_path, swap_direction)
    n_available = len(df)

    if not 1 <= n_words <= n_available:
        raise ValueError(f"Bitte eine Zahl zwischen 1 und {n_available} eingeben.")

    test_start = datetime.now()
    log_file = make_log_file(dictionary_path, test_start, log_dir)

    df = df.sample(frac=1).reset_index(drop=True)
    df = df.head(n_words)

    print("\nVokabeltest gestartet.")
    if run_label:
        print(f"Lauf: {run_label}")
    print(f"Dictionary file: {dictionary_path}")
    print(f"Verfügbare Vokabeln: {n_available}")
    print(f"Abgefragte Vokabeln: {n_words}")
    print(f"Frage-Spalte: {prompt_column}")
    print(f"Antwort-Spalte: {answer_column}")
    print(f"Logfile: {log_file}")
    print("Gib 'q' ein, um abzubrechen.\n")

    results = []

    for _, row in df.iterrows():
        prompt = row["Prompt"]
        expected_answer = row["ExpectedAnswer"]

        print(f"{prompt_column}: {prompt}")
        answer = input(f"{answer_column}: ").strip()

        if answer.lower() == "q":
            break

        is_correct = normalize_answer(answer) == normalize_answer(expected_answer)

        if is_correct:
            print("Richtig.\n")
        else:
            print(f"Falsch. Richtig wäre: {expected_answer}\n")

        results.append(
            {
                "test_start": test_start.isoformat(timespec="seconds"),
                "answer_time": datetime.now().isoformat(timespec="seconds"),
                "dictionary_file": str(dictionary_path),
                "prompt_column": prompt_column,
                "answer_column": answer_column,
                "prompt": prompt,
                "expected_answer": expected_answer,
                "given_answer": answer,
                "correct": is_correct,
            }
        )

    log_df = save_results(
        results,
        log_file,
        dictionary_path,
        prompt_column,
        answer_column,
        n_available,
        n_words,
        test_start,
    )

    if len(log_df) > 0:
        n_total = len(log_df)
        n_correct = int(log_df["correct"].sum())
        n_wrong = n_total - n_correct
        score_percent = 100 * n_correct / n_total

        print("Auswertung:")
        print(f"Dictionary file: {dictionary_path}")
        print(f"Verfügbare Vokabeln: {n_available}")
        print(f"Gewählte Vokabeln:    {n_words}")
        print(f"Tatsächlich abgefragt: {n_total}")
        print(f"Richtig: {n_correct}")
        print(f"Falsch:  {n_wrong}")
        print(f"Quote:   {score_percent:.1f}%")
        print(f"\nLogfile gespeichert als: {log_file}")

        wrong_words = log_df[log_df["correct"] == False]
        if len(wrong_words) > 0:
            print("\nFalsch beantwortete Vokabeln:")
            print(wrong_words[["prompt", "expected_answer", "given_answer"]])
    else:
        print("Keine Antworten gespeichert.")

    return {
        "log_file": log_file,
        "results": log_df,
        "dictionary_path": dictionary_path,
        "n_available": n_available,
        "n_requested": n_words,
    }


def ask_dictionary_file():
    available_dictionaries = list_dictionaries()

    if available_dictionaries:
        print("Verfügbare Dictionary-Dateien:")
        for i, path in enumerate(available_dictionaries, start=1):
            print(f"{i}. {path.name}")
        print()

    dictionary_file = input(
        "Welche Dictionary-Datei soll geladen werden? "
        "Nummer oder Dateipfad eingeben: "
    ).strip()

    return resolve_dictionary_path(dictionary_file)


def ask_yes_no(prompt, default=False):
    suffix = "J/n" if default else "j/N"
    raw = input(f"{prompt} [{suffix}] ").strip().lower()
    if not raw:
        return default
    return raw in {"j", "ja", "y", "yes"}


def ask_n_words(n_available):
    while True:
        n_words_input = input(
            f"Wie viele Vokabeln sollen abgefragt werden? [1-{n_available}] "
        ).strip()

        try:
            n_words = int(n_words_input)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
            continue

        if 1 <= n_words <= n_available:
            return n_words

        print(f"Bitte eine Zahl zwischen 1 und {n_available} eingeben.")


def main():
    dictionary_path = ask_dictionary_file()
    swap_direction = ask_yes_no("Abfragerichtung umkehren?", False)
    df, _, _ = load_dictionary(dictionary_path, swap_direction)
    n_words = ask_n_words(len(df))
    run_vocab_test(dictionary_path, n_words, swap_direction)


if __name__ == "__main__":
    main()
