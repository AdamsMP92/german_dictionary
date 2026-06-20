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

df = pd.read_csv(dictionary_path, usecols=["English", "German"])

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

log_file = f"vocab_test_log_{test_start_string}.csv"

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
print(f"Logfile: {log_file}")
print("Gib 'q' ein, um abzubrechen.\n")


for _, row in df.iterrows():
    english = row["English"]
    correct_german = row["German"]

    print(f"Englisch: {english}")
    answer = input("Deutsch: ").strip()

    if answer.lower() == "q":
        break

    is_correct = answer.lower() == correct_german.strip().lower()

    if is_correct:
        print("Richtig.\n")
    else:
        print(f"Falsch. Richtig wäre: {correct_german}\n")

    results.append({
        "test_start": test_start.isoformat(timespec="seconds"),
        "answer_time": datetime.now().isoformat(timespec="seconds"),
        "dictionary_file": str(dictionary_path),
        "English": english,
        "German_correct": correct_german,
        "German_given": answer,
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
            f.write("English,German_correct,German_given\n")

            wrong_words[["English", "German_correct", "German_given"]].to_csv(
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
        print(wrong_words[["English", "German_correct", "German_given"]])

else:
    print("Keine Antworten gespeichert.")
