import pandas as pd

words = {
    "urban": "städtisch",
    "rural": "ländlich",
    "central": "zentral",
    "nearby": "nah",
    "far": "weit",
    "crowded": "überfüllt",
    "empty": "leer",
    "busy": "belebt",
    "quiet": "ruhig",
    "loud": "laut",
    "safe": "sicher",
    "dangerous": "gefährlich",
    "clean": "sauber",
    "dirty": "schmutzig",
    "modern": "modern",
    "historic": "historisch",
    "old": "alt",
    "new": "neu",
    "public": "öffentlich",
    "private": "privat",
    "open": "offen",
    "closed": "geschlossen",
    "available": "verfügbar",
    "expensive": "teuer",
    "cheap": "günstig",
    "wide": "breit",
    "narrow": "eng",
    "straight": "gerade",
    "curved": "kurvig",
    "bright": "hell",
    "dark": "dunkel",
    "green": "grün",
    "beautiful": "schön",
    "ugly": "hässlich",
    "interesting": "interessant",
    "boring": "langweilig",
    "popular": "beliebt",
    "famous": "berühmt",
    "local": "lokal",
    "international": "international"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Stadt.csv")
