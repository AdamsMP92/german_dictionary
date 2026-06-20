import pandas as pd

words = {
    "the sun": "Die Sonne", 
    "the moon": "Der Mond", 
    "the stars": "Die Sterne", 
    "the fridge": "Der Kühlschrank", 
    "the window": "Das Fenster", 
    "the table": "Der Tisch", 
    "the chair": "Der Stuhl", 
    "the fork": "Die Gabel", 
    "the spoon": "Der Löffel",
    "the cup": "Die Tasse",
    "the plate": "Der Teller",
    "the glass": "Das Glas",
    "the marmelade": "Die Marmelade"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("dict.csv")

