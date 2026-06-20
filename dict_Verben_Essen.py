import pandas as pd

words = {
    "to eat": "essen",
    "to drink": "trinken",
    "to cook": "kochen",
    "to bake": "backen",
    "to fry": "braten",
    "to boil": "kochen",
    "to roast": "rösten",
    "to grill": "grillen",
    "to cut": "schneiden",
    "to chop": "hacken",
    "to peel": "schälen",
    "to grate": "reiben",
    "to stir": "rühren",
    "to mix": "mischen",
    "to season": "würzen",
    "to salt": "salzen",
    "to taste": "probieren",
    "to serve": "servieren",
    "to order": "bestellen",
    "to pay": "bezahlen",
    "to shop": "einkaufen",
    "to wash": "waschen",
    "to pour": "gießen",
    "to fill": "füllen",
    "to empty": "leeren",
    "to heat": "erhitzen",
    "to cool": "kühlen",
    "to freeze": "einfrieren",
    "to thaw": "auftauen",
    "to open": "öffnen",
    "to close": "schließen",
    "to share": "teilen",
    "to chew": "kauen",
    "to swallow": "schlucken",
    "to smell": "riechen",
    "to enjoy": "genießen",
    "to prefer": "bevorzugen",
    "to avoid": "vermeiden",
    "to clean up": "aufräumen",
    "to rinse": "abspülen"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("dict_Verben_Essen.csv")
