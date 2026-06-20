import pandas as pd

words = {
    "sunny": "sonnig",
    "cloudy": "bewölkt",
    "rainy": "regnerisch",
    "windy": "windig",
    "hot": "heiß",
    "cold": "kalt",
    "warm": "warm",
    "relaxed": "entspannt",
    "stressful": "stressig",
    "beautiful": "schön",
    "ugly": "hässlich",
    "interesting": "interessant",
    "boring": "langweilig",
    "comfortable": "bequem",
    "uncomfortable": "unbequem",
    "cheap": "günstig",
    "expensive": "teuer",
    "booked": "gebucht",
    "available": "verfügbar",
    "full": "voll",
    "empty": "leer",
    "early": "früh",
    "late": "spät",
    "direct": "direkt",
    "delayed": "verspätet",
    "foreign": "fremd",
    "local": "lokal",
    "safe": "sicher",
    "dangerous": "gefährlich",
    "touristy": "touristisch",
    "quiet": "ruhig",
    "loud": "laut",
    "near": "nah",
    "far": "weit",
    "clean": "sauber",
    "dirty": "schmutzig",
    "fresh": "frisch",
    "salty": "salzig",
    "deep": "tief",
    "shallow": "flach"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Urlaub.csv")
