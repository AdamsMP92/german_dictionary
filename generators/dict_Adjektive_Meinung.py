import pandas as pd

words = {
    'right': 'richtig',
    'wrong': 'falsch',
    'important': 'wichtig',
    'unimportant': 'unwichtig',
    'convincing': 'überzeugend',
    'logical': 'logisch',
    'illogical': 'unlogisch',
    'reasonable': 'vernünftig',
    'critical': 'kritisch',
    'positive': 'positiv',
    'negative': 'negativ',
    'neutral': 'neutral',
    'clear': 'klar',
    'unclear': 'unklar',
    'objective': 'objektiv',
    'subjective': 'subjektiv',
    'controversial': 'umstritten',
    'interesting': 'interessant',
    'boring': 'langweilig',
    'possible': 'möglich',
    'probable': 'wahrscheinlich',
    'doubtful': 'zweifelhaft',
    'obvious': 'offensichtlich'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Meinung.csv")
