import pandas as pd

words = {
    'to behave': 'sich verhalten',
    'to respect': 'respektieren',
    'to trust': 'vertrauen',
    'to help': 'helfen',
    'to lie': 'lügen',
    'to tell the truth': 'die Wahrheit sagen',
    'to decide': 'entscheiden',
    'to dare': 'sich trauen',
    'to give up': 'aufgeben',
    'to persist': 'durchhalten',
    'to listen': 'zuhören',
    'to share': 'teilen',
    'to forgive': 'verzeihen',
    'to apologize': 'sich entschuldigen',
    'to encourage': 'ermutigen',
    'to criticize': 'kritisieren',
    'to praise': 'loben',
    'to change': 'sich ändern',
    'to learn': 'lernen',
    'to improve': 'sich verbessern'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Charakter.csv")
