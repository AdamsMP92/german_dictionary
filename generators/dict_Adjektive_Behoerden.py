import pandas as pd

words = {
    'official': 'amtlich',
    'valid': 'gültig',
    'invalid': 'ungültig',
    'complete': 'vollständig',
    'incomplete': 'unvollständig',
    'necessary': 'notwendig',
    'personal': 'persönlich',
    'written': 'schriftlich',
    'digital': 'digital',
    'urgent': 'dringend',
    'temporary': 'vorläufig',
    'permanent': 'dauerhaft',
    'legal': 'gesetzlich',
    'responsible': 'zuständig',
    'available': 'verfügbar',
    'complicated': 'kompliziert',
    'simple': 'einfach',
    'expensive': 'teuer',
    'free': 'kostenlos',
    'current': 'aktuell'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Behoerden.csv")
