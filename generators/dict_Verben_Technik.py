import pandas as pd

words = {
    'to install': 'installieren',
    'to update': 'aktualisieren',
    'to download': 'herunterladen',
    'to upload': 'hochladen',
    'to save': 'speichern',
    'to delete': 'löschen',
    'to copy': 'kopieren',
    'to paste': 'einfügen',
    'to print': 'drucken',
    'to scan': 'scannen',
    'to charge': 'aufladen',
    'to connect': 'verbinden',
    'to disconnect': 'trennen',
    'to start': 'starten',
    'to restart': 'neu starten',
    'to shut down': 'herunterfahren',
    'to log in': 'sich anmelden',
    'to log out': 'sich abmelden',
    'to search': 'suchen',
    'to repair': 'reparieren'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Technik.csv")
