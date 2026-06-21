# German Dictionary

Ein kleiner digitaler Vokabelkasten für Deutschlernende. Die Wortlisten sind nach
Wortart und Thema sortiert und liegen als CSV-Dateien vor.

## Aktueller Umfang

Das Dictionary enthält aktuell 75 Vokabellisten mit insgesamt 2902 Einträgen:

| Wortart | Listen | Einträge |
| --- | ---: | ---: |
| Nomen mit Artikel | 25 | 1552 |
| Verben | 25 | 675 |
| Adjektive | 25 | 675 |
| Gesamt | 75 | 2902 |

## Themen

Alle Wortarten sind nach diesen Themen organisiert:

**Basis-Alltag**

| Thema | Nomen | Verben | Adjektive | Gesamt |
| --- | ---: | ---: | ---: | ---: |
| Haus | 167 | 40 | 40 | 247 |
| Essen | 100 | 40 | 40 | 180 |
| Familie | 100 | 40 | 40 | 180 |
| Kleidung | 20 | 20 | 20 | 60 |
| Koerper | 20 | 20 | 20 | 60 |
| Gesundheit | 20 | 20 | 20 | 60 |

**Handlungsfähigkeit**

| Thema | Nomen | Verben | Adjektive | Gesamt |
| --- | ---: | ---: | ---: | ---: |
| Arbeit | 100 | 40 | 40 | 180 |
| Bewerbung | 100 | 40 | 40 | 180 |
| Behoerden | 20 | 20 | 20 | 60 |
| Finanzen | 20 | 20 | 20 | 60 |
| Verkehr | 20 | 20 | 20 | 60 |
| Einkaufen | 20 | 20 | 20 | 60 |

**Ausdruck**

| Thema | Nomen | Verben | Adjektive | Gesamt |
| --- | ---: | ---: | ---: | ---: |
| Gefuehle | 25 | 23 | 23 | 71 |
| Charakter | 25 | 23 | 23 | 71 |
| Kommunikation | 20 | 20 | 20 | 60 |
| Zeit | 25 | 23 | 23 | 71 |
| Wetter | 25 | 23 | 23 | 71 |
| Meinung | 25 | 23 | 23 | 71 |

**Interessen**

| Thema | Nomen | Verben | Adjektive | Gesamt |
| --- | ---: | ---: | ---: | ---: |
| Sport | 100 | 40 | 40 | 180 |
| Urlaub | 100 | 40 | 40 | 180 |
| Hobbys | 100 | 20 | 20 | 140 |
| Medien | 100 | 20 | 20 | 140 |
| Natur | 100 | 20 | 20 | 140 |
| Technik | 100 | 20 | 20 | 140 |
| Stadt | 100 | 40 | 40 | 180 |

## Struktur

```text
generators/
  dict_Nomen_*.py
  dict_Verben_*.py
  dict_Adjektive_*.py
  generate_all.sh

csv-files/
  dict_Nomen_*.csv
  dict_Verben_*.csv
  dict_Adjektive_*.csv

test.py
pruefung.py
pixi.toml
```

Die Python-Dateien in `generators/` sind die Quellen. Die CSV-Dateien in
`csv-files/` sind die eigentlichen Vokabellisten für den Test.

## CSV-Dateien neu erzeugen

```bash
pixi run generate
```

Der Task führt `generators/generate_all.sh` aus und erzeugt alle CSV-Dateien neu.
Das Skript nutzt normales `python`, wenn Pandas verfügbar ist, und fällt sonst
auf `pixi run python` zurück.

## CSV-Dateien prüfen

```bash
pixi run validate
```

Der Validator prüft die Dictionary-Dateien auf grobe Plausibilität:

- gültiges Namensschema wie `dict_Nomen_Haus.csv`
- passende Generator-Datei
- mindestens zwei Spalten
- leere Einträge
- doppelte Fragen oder doppelte Wortpaare
- Nomen mit `the ...` und `der/die/das ...`
- Verben mit `to ...`
- Mindestanzahl pro Liste

## Manueller LanguageTool-Check

```bash
pixi run language-check
```

Dieser Developer-Check nutzt das lokal installierte `languagetool` CLI und
schreibt einen Report nach `validation_reports/languagetool_report.md`.
Standardmäßig werden nur typo-nahe LanguageTool-Regeln ausgewertet, damit kurze
Wörterbuch-Einträge nicht zu viele Grammatik-False-Positives erzeugen.

Für einen vollständigen LanguageTool-Report:

```bash
pixi run python language_check.py --all-rules
```

## Vokabeltest starten

```bash
pixi run test
```

Das Testprogramm zeigt alle CSV-Dateien aus `csv-files/` an. Danach kann eine
Liste per Nummer ausgewählt und die Anzahl der abzufragenden Wörter festgelegt
werden.

`test.py` enthält außerdem die gemeinsame Logik zum Laden, Abfragen und Loggen
eines einzelnen Vokabeltests. Das Prüfungsprogramm nutzt diese Funktionen und
startet mehrere normale Testläufe nacheinander.

## Prüfungsprogramm starten

```bash
pixi run pruefung
```

Das Prüfungsprogramm fragt eine längere Serie über mehrere Themen hinweg ab,
zum Beispiel 200 bis 500 Wörter. Dabei verteilt es die Wörter auf mehrere
passende CSV-Listen und startet pro Liste einen normalen `test.py`-Lauf. Die
Einzellogs landen weiterhin in `training_log/`.

Zusätzlich schreibt das Prüfungsprogramm eine Gesamtauswertung nach
`pruefungs_log/<lauf>/`:

- `alle_antworten.csv`
- `falsch_beantwortet.csv`
- `statistik_themen.csv`
- `statistik_wortarten.csv`
- `einzellaeufe.csv`
- `zusammenfassung.txt`

Beispiele:

```bash
pixi run pruefung --count 300 --topics Haus,Essen,Familie
pixi run pruefung --count 200 --word-types Nomen,Verben --no-reverse
pixi run pruefung --count 150 --topics Arbeit,Bewerbung --reverse
```
