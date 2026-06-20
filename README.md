# German Dictionary

Ein kleiner digitaler Vokabelkasten für Deutschlernende. Die Wortlisten sind nach
Wortart und Thema sortiert und liegen als CSV-Dateien vor.

## Aktueller Umfang

Das Dictionary enthält aktuell 24 Vokabellisten mit insgesamt 1507 Einträgen:

| Wortart | Listen | Einträge |
| --- | ---: | ---: |
| Nomen mit Artikel | 8 | 867 |
| Verben | 8 | 320 |
| Adjektive | 8 | 320 |
| Gesamt | 24 | 1507 |

## Themen

Alle Wortarten sind nach diesen Themen organisiert:

- Arbeit
- Bewerbung
- Essen
- Familie
- Haus
- Sport
- Stadt
- Urlaub

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
pixi.toml
```

Die Python-Dateien in `generators/` sind die Quellen. Die CSV-Dateien in
`csv-files/` sind die eigentlichen Vokabellisten für den Test.

## CSV-Dateien neu erzeugen

```bash
generators/generate_all.sh
```

Das Skript erzeugt alle CSV-Dateien neu. Es nutzt normales `python`, wenn Pandas
verfügbar ist, und fällt sonst auf `pixi run python` zurück.

## Vokabeltest starten

```bash
pixi run test
```

Das Testprogramm zeigt alle CSV-Dateien aus `csv-files/` an. Danach kann eine
Liste per Nummer ausgewählt und die Anzahl der abzufragenden Wörter festgelegt
werden.
