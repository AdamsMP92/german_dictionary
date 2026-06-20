import pandas as pd

words = {
    'to wait': 'warten',
    'to hurry': 'sich beeilen',
    'to delay': 'verzögern',
    'to postpone': 'verschieben',
    'to plan': 'planen',
    'to schedule': 'terminieren',
    'to begin': 'beginnen',
    'to end': 'enden',
    'to last': 'dauern',
    'to repeat': 'wiederholen',
    'to remember': 'sich erinnern',
    'to forget': 'vergessen',
    'to arrive early': 'früh ankommen',
    'to be late': 'spät dran sein',
    'to spend time': 'Zeit verbringen',
    'to save time': 'Zeit sparen',
    'to waste time': 'Zeit verschwenden',
    'to count': 'zählen',
    'to measure': 'messen',
    'to pause': 'pausieren'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Zeit.csv")
