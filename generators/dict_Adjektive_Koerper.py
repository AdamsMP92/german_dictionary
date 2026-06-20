import pandas as pd

words = {
    'healthy': 'gesund',
    'sick': 'krank',
    'strong': 'stark',
    'weak': 'schwach',
    'tired': 'müde',
    'awake': 'wach',
    'fit': 'fit',
    'injured': 'verletzt',
    'painful': 'schmerzhaft',
    'sensitive': 'empfindlich',
    'warm': 'warm',
    'cold': 'kalt',
    'numb': 'taub',
    'swollen': 'geschwollen',
    'relaxed': 'entspannt',
    'tense': 'angespannt',
    'upright': 'aufrecht',
    'crooked': 'krumm',
    'flexible': 'beweglich',
    'stiff': 'steif'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Koerper.csv")
