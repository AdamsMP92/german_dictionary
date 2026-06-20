import pandas as pd

words = {
    "to apply": "sich bewerben",
    "to search": "suchen",
    "to find": "finden",
    "to read": "lesen",
    "to write": "schreiben",
    "to attach": "anhängen",
    "to upload": "hochladen",
    "to send": "senden",
    "to introduce oneself": "sich vorstellen",
    "to describe": "beschreiben",
    "to explain": "erklären",
    "to mention": "erwähnen",
    "to emphasize": "betonen",
    "to prepare": "vorbereiten",
    "to research": "recherchieren",
    "to practice": "üben",
    "to answer": "antworten",
    "to ask": "fragen",
    "to invite": "einladen",
    "to confirm": "bestätigen",
    "to postpone": "verschieben",
    "to cancel": "absagen",
    "to appear": "erscheinen",
    "to arrive": "ankommen",
    "to greet": "begrüßen",
    "to convince": "überzeugen",
    "to impress": "beeindrucken",
    "to offer": "anbieten",
    "to accept": "annehmen",
    "to decline": "ablehnen",
    "to negotiate": "verhandeln",
    "to sign": "unterschreiben",
    "to start": "anfangen",
    "to begin": "beginnen",
    "to change jobs": "den Job wechseln",
    "to gain experience": "Erfahrung sammeln",
    "to qualify": "sich qualifizieren",
    "to recommend": "empfehlen",
    "to wait": "warten",
    "to follow up": "nachfragen"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Bewerbung.csv")
