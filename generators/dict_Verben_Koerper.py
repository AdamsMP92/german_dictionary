import pandas as pd

words = {
    'to breathe': 'atmen',
    'to see': 'sehen',
    'to hear': 'hören',
    'to smell': 'riechen',
    'to taste': 'schmecken',
    'to touch': 'berühren',
    'to feel': 'fühlen',
    'to stand': 'stehen',
    'to sit': 'sitzen',
    'to lie': 'liegen',
    'to walk': 'gehen',
    'to run': 'laufen',
    'to bend': 'beugen',
    'to stretch': 'strecken',
    'to blink': 'blinzeln',
    'to swallow': 'schlucken',
    'to cough': 'husten',
    'to sneeze': 'niesen',
    'to sweat': 'schwitzen',
    'to shiver': 'zittern'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Koerper.csv")
