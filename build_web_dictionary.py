import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


CSV_DIR = Path("csv-files")
DOCS_DIR = Path("docs")
OUTPUT_FILE = DOCS_DIR / "dictionary.json"
WORD_TYPES = ["Nomen", "Verben", "Adjektive"]


def build_dictionary():
    entries = []
    summary = defaultdict(Counter)

    for path in sorted(CSV_DIR.glob("dict_*.csv")):
        _, word_type, topic = path.stem.split("_", 2)
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                english = (row.get("English") or "").strip()
                german = (row.get("German") or "").strip()
                if not english or not german:
                    continue

                entries.append(
                    {
                        "topic": topic,
                        "wordType": word_type,
                        "english": english,
                        "german": german,
                        "source": path.name,
                    }
                )
                summary[topic][word_type] += 1

    topics = []
    for topic in sorted(summary):
        counts = {word_type: summary[topic][word_type] for word_type in WORD_TYPES}
        counts["Gesamt"] = sum(counts.values())
        topics.append({"name": topic, "counts": counts})

    return {
        "generatedFrom": str(CSV_DIR),
        "total": len(entries),
        "wordTypes": WORD_TYPES,
        "topics": topics,
        "entries": entries,
    }


def main():
    DOCS_DIR.mkdir(exist_ok=True)
    data = build_dictionary()
    OUTPUT_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT_FILE} with {data['total']} entries.")


if __name__ == "__main__":
    main()
