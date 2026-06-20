import pandas as pd

words = {
    'digital': 'digital',
    'printed': 'gedruckt',
    'online': 'online',
    'offline': 'offline',
    'public': 'öffentlich',
    'private': 'privat',
    'current': 'aktuell',
    'old': 'alt',
    'reliable': 'zuverlässig',
    'unreliable': 'unzuverlässig',
    'popular': 'beliebt',
    'viral': 'viral',
    'visible': 'sichtbar',
    'hidden': 'versteckt',
    'short': 'kurz',
    'long': 'lang',
    'interesting': 'interessant',
    'boring': 'langweilig',
    'critical': 'kritisch',
    'neutral': 'neutral'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Medien.csv")
