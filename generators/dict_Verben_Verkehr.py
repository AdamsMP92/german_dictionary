import pandas as pd

words = {
    'to drive': 'fahren',
    'to ride': 'mitfahren',
    'to walk': 'gehen',
    'to wait': 'warten',
    'to change': 'umsteigen',
    'to get in': 'einsteigen',
    'to get out': 'aussteigen',
    'to miss': 'verpassen',
    'to arrive': 'ankommen',
    'to depart': 'abfahren',
    'to park': 'parken',
    'to brake': 'bremsen',
    'to turn': 'abbiegen',
    'to overtake': 'überholen',
    'to cross': 'überqueren',
    'to buy a ticket': 'eine Fahrkarte kaufen',
    'to validate': 'entwerten',
    'to reserve': 'reservieren',
    'to be delayed': 'sich verspäten',
    'to navigate': 'navigieren'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Verkehr.csv")
