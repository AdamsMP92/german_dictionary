import pandas as pd

words = {
    'to wear': 'tragen',
    'to put on': 'anziehen',
    'to take off': 'ausziehen',
    'to try on': 'anprobieren',
    'to fit': 'passen',
    'to wash': 'waschen',
    'to dry': 'trocknen',
    'to iron': 'bügeln',
    'to fold': 'falten',
    'to hang up': 'aufhängen',
    'to sew': 'nähen',
    'to button': 'zuknöpfen',
    'to zip up': 'zumachen',
    'to change clothes': 'sich umziehen',
    'to buy': 'kaufen',
    'to return': 'zurückgeben',
    'to choose': 'auswählen',
    'to combine': 'kombinieren',
    'to match': 'zusammenpassen',
    'to shrink': 'einlaufen'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Kleidung.csv")
