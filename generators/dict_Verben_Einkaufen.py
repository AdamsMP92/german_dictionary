import pandas as pd

words = {
    'to shop': 'einkaufen',
    'to buy': 'kaufen',
    'to sell': 'verkaufen',
    'to pay': 'bezahlen',
    'to choose': 'auswählen',
    'to look for': 'suchen',
    'to find': 'finden',
    'to compare': 'vergleichen',
    'to try on': 'anprobieren',
    'to order': 'bestellen',
    'to return': 'zurückgeben',
    'to exchange': 'umtauschen',
    'to ask': 'fragen',
    'to recommend': 'empfehlen',
    'to weigh': 'wiegen',
    'to pack': 'einpacken',
    'to scan': 'scannen',
    'to cost': 'kosten',
    'to reduce': 'reduzieren',
    'to save': 'sparen'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Einkaufen.csv")
