import pandas as pd
from datetime import datetime
from pathlib import Path


# ------------------------------------------------------------
# Dictionary-Datei auswählen
# ------------------------------------------------------------

dictionary_dir = Path("csv-files")
available_dictionaries = sorted(dictionary_dir.glob("*.csv"))

if available_dictionaries:
    print("Verfügbare Dictionary-Dateien:")
    for i, path in enumerate(available_dictionaries, start=1):
        print(f"{i}. {path.name}")
    print()

dictionary_file = input(
    "Welche Dictionary-Datei soll geladen werden? "
    "Nummer oder Dateipfad eingeben: "
).strip()

if dictionary_file.isdigit() and available_dictionaries:
    selected_index = int(dictionary_file) - 1
    if not 0 <= selected_index < len(available_dictionaries):
        raise ValueError("Ungültige Dictionary-Nummer.")
    dictionary_path = available_dictionaries[selected_index]
else:
    dictionary_path = Path(dictionary_file)
    if not dictionary_path.exists():
        dictionary_path = dictionary_dir / dictionary_file

if not dictionary_path.exists():
    raise FileNotFoundError(f"Dictionary file nicht gefunden: {dictionary_file}")


# ------------------------------------------------------------
# Dictionary laden
# ------------------------------------------------------------

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

swap_input = input(
    "Abfragerichtung umkehren? [j/N] "
).strip().lower()

if swap_input in {"j", "ja", "y", "yes"}:
    prompt_column, answer_column = answer_column, prompt_column
    df = df.rename(
        columns={
            "Prompt": "ExpectedAnswer",
            "ExpectedAnswer": "Prompt",
        }
    )

n_available = len(df)

if n_available == 0:
    raise ValueError(f"Dictionary file ist leer: {dictionary_file}")


# ------------------------------------------------------------
# Anzahl der abzufragenden Vokabeln auswählen
# ------------------------------------------------------------

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
        break

    print(f"Bitte eine Zahl zwischen 1 und {n_available} eingeben.")


# ------------------------------------------------------------
# Test vorbereiten
# ------------------------------------------------------------

test_start = datetime.now()
test_start_string = test_start.strftime("%Y-%m-%d_%H-%M-%S")

log_dir = Path("training_log")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / f"vocab_test_log_{test_start_string}.csv"

df = df.sample(frac=1).reset_index(drop=True)
df = df.head(n_words)

results = []


# ------------------------------------------------------------
# Vokabeltest durchführen
# ------------------------------------------------------------

print("\nVokabeltest gestartet.")
print(f"Dictionary file: {dictionary_path}")
print(f"Verfügbare Vokabeln: {n_available}")
print(f"Abgefragte Vokabeln: {n_words}")
print(f"Frage-Spalte: {prompt_column}")
print(f"Antwort-Spalte: {answer_column}")
print(f"Logfile: {log_file}")
print("Gib 'q' ein, um abzubrechen.\n")


for _, row in df.iterrows():
    prompt = row["Prompt"]
    expected_answer = row["ExpectedAnswer"]

    print(f"{prompt_column}: {prompt}")
    answer = input(f"{answer_column}: ").strip()

    if answer.lower() == "q":
        break

    is_correct = answer.lower() == str(expected_answer).strip().lower()

    if is_correct:
        print("Richtig.\n")
    else:
        print(f"Falsch. Richtig wäre: {expected_answer}\n")

    results.append({
        "test_start": test_start.isoformat(timespec="seconds"),
        "answer_time": datetime.now().isoformat(timespec="seconds"),
        "dictionary_file": str(dictionary_path),
        "prompt_column": prompt_column,
        "answer_column": answer_column,
        "prompt": prompt,
        "expected_answer": expected_answer,
        "given_answer": answer,
        "correct": is_correct,
    })


# ------------------------------------------------------------
# Ergebnisse auswerten und speichern
# ------------------------------------------------------------

log_df = pd.DataFrame(results)

if len(log_df) > 0:
    n_total = len(log_df)
    n_correct = int(log_df["correct"].sum())
    n_wrong = n_total - n_correct
    score_percent = 100 * n_correct / n_total

    wrong_words = log_df[log_df["correct"] == False]

    # Einzelantworten speichern
    log_df.to_csv(log_file, index=False)

    # Statistik an dieselbe Logfile anhängen
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

    print("Auswertung:")
    print(f"Dictionary file: {dictionary_path}")
    print(f"Verfügbare Vokabeln: {n_available}")
    print(f"Gewählte Vokabeln:    {n_words}")
    print(f"Tatsächlich abgefragt: {n_total}")
    print(f"Richtig: {n_correct}")
    print(f"Falsch:  {n_wrong}")
    print(f"Quote:   {score_percent:.1f}%")
    print(f"\nLogfile gespeichert als: {log_file}")

    if len(wrong_words) > 0:
        print("\nFalsch beantwortete Vokabeln:")
        print(wrong_words[["prompt", "expected_answer", "given_answer"]])

else:
    print("Keine Antworten gespeichert.")
