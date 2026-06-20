import argparse
import csv
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import pandas as pd

from test import DICTIONARY_DIR, load_dictionary, list_dictionaries, run_vocab_test


PRUEFUNGS_LOG_DIR = Path("pruefungs_log")
FILENAME_PATTERN = re.compile(r"^dict_(Nomen|Verben|Adjektive)_(.+)\.csv$")


def parse_list(value):
    if not value:
        return None
    return {part.strip() for part in value.split(",") if part.strip()}


def ask_int(prompt, default, minimum, maximum):
    while True:
        raw = input(f"{prompt} [{default}]: ").strip()
        if not raw:
            return default
        try:
            value = int(raw)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Bitte eine Zahl zwischen {minimum} und {maximum} eingeben.")


def ask_yes_no(prompt, default=False):
    suffix = "J/n" if default else "j/N"
    while True:
        raw = input(f"{prompt} [{suffix}]: ").strip().lower()
        if not raw:
            return default
        if raw in {"j", "ja", "y", "yes"}:
            return True
        if raw in {"n", "nein", "no"}:
            return False
        print("Bitte j oder n eingeben.")


def dictionary_metadata(path):
    match = FILENAME_PATTERN.match(path.name)
    if not match:
        return None
    word_type, topic = match.groups()
    return {
        "path": path,
        "word_type": word_type,
        "topic": topic,
        "rows": len(load_dictionary(path)[0]),
    }


def list_dictionary_metadata():
    metadata = []
    for path in list_dictionaries(DICTIONARY_DIR):
        item = dictionary_metadata(path)
        if item:
            metadata.append(item)
    return metadata


def filter_dictionaries(metadata, topics=None, word_types=None):
    selected = []
    for item in metadata:
        if topics and item["topic"] not in topics:
            continue
        if word_types and item["word_type"] not in word_types:
            continue
        selected.append(item)
    return selected


def allocate_words(selected, total_count):
    selected = [item.copy() for item in selected if item["rows"] > 0]
    remaining = min(total_count, sum(item["rows"] for item in selected))
    allocations = []

    while remaining > 0 and selected:
        active = [item for item in selected if item["rows"] > item.get("assigned", 0)]
        if not active:
            break
        per_file = max(1, remaining // len(active))
        for item in active:
            if remaining <= 0:
                break
            free = item["rows"] - item.get("assigned", 0)
            amount = min(per_file, free, remaining)
            item["assigned"] = item.get("assigned", 0) + amount
            remaining -= amount

    for item in selected:
        assigned = item.get("assigned", 0)
        if assigned:
            item["assigned"] = assigned
            allocations.append(item)

    return allocations


def summarize_by(rows, field):
    stats = defaultdict(lambda: {"total": 0, "correct": 0, "wrong": 0})
    for row in rows:
        key = row[field]
        stats[key]["total"] += 1
        if bool(row["correct"]):
            stats[key]["correct"] += 1
        else:
            stats[key]["wrong"] += 1
    return stats


def write_stats(path, stats, label):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[label, "total", "correct", "wrong", "score_percent"],
        )
        writer.writeheader()
        for key in sorted(stats):
            total = stats[key]["total"]
            correct = stats[key]["correct"]
            score = 100 * correct / total if total else 0
            writer.writerow(
                {
                    label: key,
                    "total": total,
                    "correct": correct,
                    "wrong": stats[key]["wrong"],
                    "score_percent": f"{score:.1f}",
                }
            )


def write_pruefungs_logs(run_dir, all_results, run_logs, settings, started_at, finished_at):
    run_dir.mkdir(parents=True, exist_ok=True)
    all_answers_file = run_dir / "alle_antworten.csv"
    wrong_file = run_dir / "falsch_beantwortet.csv"
    topic_stats_file = run_dir / "statistik_themen.csv"
    word_type_stats_file = run_dir / "statistik_wortarten.csv"
    run_logs_file = run_dir / "einzellaeufe.csv"
    summary_file = run_dir / "zusammenfassung.txt"

    if all_results:
        all_df = pd.concat(all_results, ignore_index=True)
    else:
        all_df = pd.DataFrame()

    all_df.to_csv(all_answers_file, index=False)
    if "correct" in all_df:
        all_df[all_df["correct"] == False].to_csv(wrong_file, index=False)
    else:
        all_df.to_csv(wrong_file, index=False)

    rows = all_df.to_dict("records")
    write_stats(topic_stats_file, summarize_by(rows, "topic"), "topic")
    write_stats(word_type_stats_file, summarize_by(rows, "word_type"), "word_type")

    with run_logs_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "dictionary_file",
                "word_type",
                "topic",
                "requested_words",
                "answered_words",
                "log_file",
            ],
        )
        writer.writeheader()
        writer.writerows(run_logs)

    total = len(all_df)
    correct = int(all_df["correct"].sum()) if "correct" in all_df else 0
    wrong = total - correct
    score = 100 * correct / total if total else 0

    with summary_file.open("w", encoding="utf-8") as f:
        f.write("Pruefungsprogramm Zusammenfassung\n")
        f.write("=================================\n\n")
        f.write(f"Start: {started_at.isoformat(timespec='seconds')}\n")
        f.write(f"Ende:  {finished_at.isoformat(timespec='seconds')}\n")
        f.write(f"Dauer: {finished_at - started_at}\n\n")
        for key, value in settings.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")
        f.write(f"Einzellaeufe: {len(run_logs)}\n")
        f.write(f"Abgefragt:    {total}\n")
        f.write(f"Richtig:      {correct}\n")
        f.write(f"Falsch:       {wrong}\n")
        f.write(f"Quote:        {score:.1f}%\n")

    return {
        "summary": summary_file,
        "all_answers": all_answers_file,
        "wrong": wrong_file,
        "topic_stats": topic_stats_file,
        "word_type_stats": word_type_stats_file,
        "run_logs": run_logs_file,
        "total": total,
        "correct": correct,
        "wrong_count": wrong,
        "score": score,
    }


def configure(args, metadata):
    topics = sorted({item["topic"] for item in metadata})
    word_types = ["Nomen", "Verben", "Adjektive"]

    print("Pruefungsprogramm")
    print("=================")
    print("Dieses Programm steuert mehrere normale test.py-Laeufe.")
    print(f"Verfügbare Listen: {len(metadata)}")
    print(f"Themen: {', '.join(topics)}")
    print(f"Wortarten: {', '.join(word_types)}")
    print()

    topics_filter = parse_list(args.topics)
    if topics_filter is None and ask_yes_no("Nur bestimmte Themen auswählen?", False):
        print("Mehrere Themen mit Komma trennen.")
        topics_filter = parse_list(input("Themen: ").strip())

    word_type_filter = parse_list(args.word_types)
    if word_type_filter is None and ask_yes_no("Nur bestimmte Wortarten auswählen?", False):
        print("Möglich sind: Nomen, Verben, Adjektive. Mehrere mit Komma trennen.")
        word_type_filter = parse_list(input("Wortarten: ").strip())

    selected = filter_dictionaries(metadata, topics_filter, word_type_filter)
    if not selected:
        raise ValueError("Nach der Auswahl sind keine Dictionary-Listen übrig.")

    max_words = sum(item["rows"] for item in selected)
    count = args.count or ask_int("Wie viele Wörter insgesamt?", min(300, max_words), 1, max_words)
    count = min(count, max_words)

    swap_direction = args.reverse
    if swap_direction is None:
        swap_direction = ask_yes_no("Abfragerichtung umkehren?", False)

    return selected, count, swap_direction, topics_filter, word_type_filter


def main():
    parser = argparse.ArgumentParser(
        description="Steuert mehrere test.py-Laeufe über Themen und Wortarten hinweg."
    )
    parser.add_argument("--count", type=int, help="Anzahl der Wörter insgesamt.")
    parser.add_argument("--topics", help="Kommagetrennte Themen, z.B. Haus,Essen,Arbeit.")
    parser.add_argument("--word-types", help="Kommagetrennte Wortarten: Nomen,Verben,Adjektive.")
    parser.add_argument(
        "--reverse",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Abfragerichtung von Deutsch nach Englisch umkehren.",
    )
    args = parser.parse_args()

    metadata = list_dictionary_metadata()
    if not metadata:
        raise FileNotFoundError(f"Keine Dictionary CSV-Dateien gefunden in {DICTIONARY_DIR}.")

    selected, count, swap_direction, topics_filter, word_type_filter = configure(args, metadata)
    allocations = allocate_words(selected, count)

    started_at = datetime.now()
    run_dir = PRUEFUNGS_LOG_DIR / started_at.strftime("pruefung_%Y-%m-%d_%H-%M-%S")
    all_results = []
    run_logs = []

    print()
    print("Prüfung gestartet.")
    print(f"Gesamtwörter: {sum(item['assigned'] for item in allocations)}")
    print(f"Einzelläufe:  {len(allocations)}")
    print(f"Log-Ordner:   {run_dir}")
    print()

    for index, item in enumerate(allocations, start=1):
        run_label = f"{index}/{len(allocations)} - {item['word_type']} / {item['topic']}"
        result = run_vocab_test(
            item["path"],
            item["assigned"],
            swap_direction=swap_direction,
            run_label=run_label,
        )

        result_df = result["results"].copy()
        if len(result_df) > 0:
            result_df["word_type"] = item["word_type"]
            result_df["topic"] = item["topic"]
            all_results.append(result_df)

        run_logs.append(
            {
                "dictionary_file": str(item["path"]),
                "word_type": item["word_type"],
                "topic": item["topic"],
                "requested_words": item["assigned"],
                "answered_words": len(result_df),
                "log_file": str(result["log_file"]),
            }
        )

        if len(result_df) < item["assigned"]:
            print("Prüfung abgebrochen.")
            break

    finished_at = datetime.now()
    settings = {
        "Gewünschte Wörter": count,
        "Themenfilter": ", ".join(sorted(topics_filter)) if topics_filter else "alle",
        "Wortartfilter": ", ".join(sorted(word_type_filter)) if word_type_filter else "alle",
        "Abfragerichtung": "Deutsch -> Englisch" if swap_direction else "Englisch -> Deutsch",
    }
    log_info = write_pruefungs_logs(run_dir, all_results, run_logs, settings, started_at, finished_at)

    print()
    print("Gesamtauswertung:")
    print(f"Abgefragt: {log_info['total']}")
    print(f"Richtig:   {log_info['correct']}")
    print(f"Falsch:    {log_info['wrong_count']}")
    print(f"Quote:     {log_info['score']:.1f}%")
    print()
    print("Prüfungs-Logfiles:")
    print(f"- {log_info['summary']}")
    print(f"- {log_info['all_answers']}")
    print(f"- {log_info['wrong']}")
    print(f"- {log_info['topic_stats']}")
    print(f"- {log_info['word_type_stats']}")
    print(f"- {log_info['run_logs']}")


if __name__ == "__main__":
    main()
