import pandas as pd

words = {
    "hungry": "hungrig",
    "thirsty": "durstig",
    "delicious": "lecker",
    "tasty": "schmackhaft",
    "fresh": "frisch",
    "old": "alt",
    "hot": "heiß",
    "cold": "kalt",
    "warm": "warm",
    "raw": "roh",
    "cooked": "gekocht",
    "fried": "gebraten",
    "baked": "gebacken",
    "sweet": "süß",
    "sour": "sauer",
    "salty": "salzig",
    "bitter": "bitter",
    "spicy": "scharf",
    "mild": "mild",
    "creamy": "cremig",
    "crispy": "knusprig",
    "soft": "weich",
    "hard": "hart",
    "juicy": "saftig",
    "dry": "trocken",
    "healthy": "gesund",
    "unhealthy": "ungesund",
    "vegetarian": "vegetarisch",
    "vegan": "vegan",
    "organic": "biologisch",
    "homemade": "hausgemacht",
    "ready-made": "fertig",
    "cheap": "günstig",
    "expensive": "teuer",
    "small": "klein",
    "large": "groß",
    "full": "satt",
    "empty": "leer",
    "light": "leicht",
    "heavy": "schwer"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Essen.csv")
