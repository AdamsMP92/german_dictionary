import pandas as pd

words = {
    'to think': 'denken',
    'to believe': 'glauben',
    'to mean': 'meinen',
    'to agree': 'zustimmen',
    'to disagree': 'widersprechen',
    'to argue': 'argumentieren',
    'to explain': 'erklären',
    'to justify': 'begründen',
    'to criticize': 'kritisieren',
    'to praise': 'loben',
    'to compare': 'vergleichen',
    'to decide': 'entscheiden',
    'to doubt': 'zweifeln',
    'to convince': 'überzeugen',
    'to discuss': 'diskutieren',
    'to suggest': 'vorschlagen',
    'to reject': 'ablehnen',
    'to accept': 'akzeptieren',
    'to conclude': 'schlussfolgern',
    'to evaluate': 'bewerten'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Meinung.csv")
