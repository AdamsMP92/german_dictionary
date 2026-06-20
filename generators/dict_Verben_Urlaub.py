import pandas as pd

words = {
    "to travel": "reisen",
    "to book": "buchen",
    "to reserve": "reservieren",
    "to pack": "packen",
    "to unpack": "auspacken",
    "to depart": "abreisen",
    "to arrive": "ankommen",
    "to fly": "fliegen",
    "to land": "landen",
    "to check in": "einchecken",
    "to check out": "auschecken",
    "to board": "einsteigen",
    "to transfer": "umsteigen",
    "to rent": "mieten",
    "to drive": "fahren",
    "to hike": "wandern",
    "to swim": "schwimmen",
    "to sunbathe": "sich sonnen",
    "to relax": "sich entspannen",
    "to rest": "sich ausruhen",
    "to visit": "besichtigen",
    "to photograph": "fotografieren",
    "to film": "filmen",
    "to explore": "erkunden",
    "to discover": "entdecken",
    "to get lost": "sich verlaufen",
    "to ask": "fragen",
    "to translate": "übersetzen",
    "to order": "bestellen",
    "to pay": "bezahlen",
    "to exchange money": "Geld wechseln",
    "to swim out": "hinausschwimmen",
    "to dive": "tauchen",
    "to snorkel": "schnorcheln",
    "to camp": "campen",
    "to send": "schicken",
    "to buy": "kaufen",
    "to complain": "sich beschweren",
    "to insure": "versichern",
    "to return": "zurückkehren"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Urlaub.csv")
