import pandas as pd

words = {
    'digital': 'digital',
    'analog': 'analog',
    'automatic': 'automatisch',
    'manual': 'manuell',
    'wireless': 'kabellos',
    'connected': 'verbunden',
    'secure': 'sicher',
    'insecure': 'unsicher',
    'fast': 'schnell',
    'slow': 'langsam',
    'new': 'neu',
    'old': 'alt',
    'broken': 'kaputt',
    'compatible': 'kompatibel',
    'available': 'verfügbar',
    'online': 'online',
    'offline': 'offline',
    'technical': 'technisch',
    'useful': 'nützlich',
    'complicated': 'kompliziert'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Technik.csv")
