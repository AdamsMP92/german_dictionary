import pandas as pd

words = {
    "fit": "fit",
    "strong": "stark",
    "weak": "schwach",
    "fast": "schnell",
    "slow": "langsam",
    "active": "aktiv",
    "tired": "müde",
    "exhausted": "erschöpft",
    "healthy": "gesund",
    "injured": "verletzt",
    "flexible": "beweglich",
    "stiff": "steif",
    "athletic": "sportlich",
    "competitive": "wettbewerbsorientiert",
    "fair": "fair",
    "unfair": "unfair",
    "successful": "erfolgreich",
    "defeated": "besiegt",
    "motivated": "motiviert",
    "focused": "konzentriert",
    "nervous": "nervös",
    "calm": "ruhig",
    "dangerous": "gefährlich",
    "safe": "sicher",
    "difficult": "schwierig",
    "easy": "einfach",
    "regular": "regelmäßig",
    "irregular": "unregelmäßig",
    "professional": "professionell",
    "amateur": "amateurhaft",
    "indoor": "drinnen",
    "outdoor": "draußen",
    "wet": "nass",
    "dry": "trocken",
    "heavy": "schwer",
    "light": "leicht",
    "short": "kurz",
    "long": "lang",
    "intense": "intensiv",
    "relaxed": "entspannt"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Sport.csv")
