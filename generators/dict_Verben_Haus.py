import pandas as pd

words = {
    "to live": "wohnen",
    "to enter": "eintreten",
    "to leave": "verlassen",
    "to open": "öffnen",
    "to close": "schließen",
    "to lock": "abschließen",
    "to unlock": "aufschließen",
    "to clean": "putzen",
    "to tidy up": "aufräumen",
    "to vacuum": "staubsaugen",
    "to sweep": "kehren",
    "to mop": "wischen",
    "to dust": "Staub wischen",
    "to wash": "waschen",
    "to dry": "trocknen",
    "to iron": "bügeln",
    "to fold": "falten",
    "to hang up": "aufhängen",
    "to repair": "reparieren",
    "to fix": "in Ordnung bringen",
    "to drill": "bohren",
    "to screw": "schrauben",
    "to hammer": "hämmern",
    "to measure": "messen",
    "to paint": "streichen",
    "to decorate": "dekorieren",
    "to move furniture": "Möbel rücken",
    "to cook": "kochen",
    "to bake": "backen",
    "to rinse": "abspülen",
    "to load": "beladen",
    "to unload": "entladen",
    "to turn on": "einschalten",
    "to turn off": "ausschalten",
    "to heat": "heizen",
    "to ventilate": "lüften",
    "to water": "gießen",
    "to plant": "pflanzen",
    "to store": "lagern",
    "to throw away": "wegwerfen"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Haus.csv")
