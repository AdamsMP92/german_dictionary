import pandas as pd

words = {
    'early': 'früh',
    'late': 'spät',
    'punctual': 'pünktlich',
    'delayed': 'verspätet',
    'fast': 'schnell',
    'slow': 'langsam',
    'short': 'kurz',
    'long': 'lang',
    'daily': 'täglich',
    'weekly': 'wöchentlich',
    'monthly': 'monatlich',
    'annual': 'jährlich',
    'current': 'aktuell',
    'past': 'vergangen',
    'future': 'zukünftig',
    'temporary': 'vorübergehend',
    'permanent': 'dauerhaft',
    'regular': 'regelmäßig',
    'rare': 'selten',
    'frequent': 'häufig',
    'immediate': 'sofortig',
    'previous': 'vorherig',
    'following': 'folgend'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Zeit.csv")
