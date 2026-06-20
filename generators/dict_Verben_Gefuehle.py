import pandas as pd

words = {
    'to feel': 'fühlen',
    'to be happy': 'sich freuen',
    'to cry': 'weinen',
    'to laugh': 'lachen',
    'to fear': 'sich fürchten',
    'to worry': 'sich sorgen',
    'to hope': 'hoffen',
    'to love': 'lieben',
    'to hate': 'hassen',
    'to trust': 'vertrauen',
    'to doubt': 'zweifeln',
    'to miss': 'vermissen',
    'to calm down': 'sich beruhigen',
    'to relax': 'sich entspannen',
    'to annoy': 'ärgern',
    'to be ashamed': 'sich schämen',
    'to surprise': 'überraschen',
    'to enjoy': 'genießen',
    'to suffer': 'leiden',
    'to motivate': 'motivieren'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Gefuehle.csv")
