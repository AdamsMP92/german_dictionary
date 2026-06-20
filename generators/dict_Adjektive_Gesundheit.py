import pandas as pd

words = {
    'ill': 'krank',
    'healthy': 'gesund',
    'contagious': 'ansteckend',
    'chronic': 'chronisch',
    'acute': 'akut',
    'painful': 'schmerzhaft',
    'mild': 'leicht',
    'severe': 'schwer',
    'medical': 'medizinisch',
    'insured': 'versichert',
    'dizzy': 'schwindelig',
    'nauseous': 'übel',
    'allergic': 'allergisch',
    'infected': 'infiziert',
    'stable': 'stabil',
    'weak': 'schwach',
    'pale': 'blass',
    'feverish': 'fiebrig',
    'necessary': 'notwendig',
    'urgent': 'dringend'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Gesundheit.csv")
