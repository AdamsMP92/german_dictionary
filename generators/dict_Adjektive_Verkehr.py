import pandas as pd

words = {
    'fast': 'schnell',
    'slow': 'langsam',
    'late': 'verspätet',
    'punctual': 'pünktlich',
    'crowded': 'überfüllt',
    'empty': 'leer',
    'direct': 'direkt',
    'indirect': 'indirekt',
    'near': 'nah',
    'far': 'weit',
    'safe': 'sicher',
    'dangerous': 'gefährlich',
    'valid': 'gültig',
    'invalid': 'ungültig',
    'one-way': 'einfach',
    'return': 'hin und zurück',
    'public': 'öffentlich',
    'private': 'privat',
    'electric': 'elektrisch',
    'automatic': 'automatisch'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Verkehr.csv")
