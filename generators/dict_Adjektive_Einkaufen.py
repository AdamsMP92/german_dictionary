import pandas as pd

words = {
    'cheap': 'günstig',
    'expensive': 'teuer',
    'fresh': 'frisch',
    'new': 'neu',
    'used': 'gebraucht',
    'available': 'verfügbar',
    'sold out': 'ausverkauft',
    'reduced': 'reduziert',
    'popular': 'beliebt',
    'practical': 'praktisch',
    'small': 'klein',
    'large': 'groß',
    'colorful': 'bunt',
    'plain': 'einfarbig',
    'open': 'offen',
    'closed': 'geschlossen',
    'friendly': 'freundlich',
    'helpful': 'hilfreich',
    'modern': 'modern',
    'local': 'lokal'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Einkaufen.csv")
