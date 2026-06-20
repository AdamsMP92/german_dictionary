import pandas as pd

words = {
    "important": "wichtig",
    "urgent": "dringend",
    "professional": "professionell",
    "reliable": "zuverlässig",
    "punctual": "pünktlich",
    "productive": "produktiv",
    "efficient": "effizient",
    "organized": "organisiert",
    "flexible": "flexibel",
    "responsible": "verantwortlich",
    "experienced": "erfahren",
    "qualified": "qualifiziert",
    "creative": "kreativ",
    "independent": "selbstständig",
    "team-oriented": "teamorientiert",
    "friendly": "freundlich",
    "polite": "höflich",
    "clear": "klar",
    "confusing": "verwirrend",
    "difficult": "schwierig",
    "simple": "einfach",
    "complex": "komplex",
    "successful": "erfolgreich",
    "stressful": "stressig",
    "busy": "beschäftigt",
    "available": "verfügbar",
    "absent": "abwesend",
    "present": "anwesend",
    "finished": "fertig",
    "unfinished": "unfertig",
    "expensive": "teuer",
    "cheap": "günstig",
    "profitable": "profitabel",
    "useful": "nützlich",
    "necessary": "notwendig",
    "optional": "optional",
    "digital": "digital",
    "manual": "manuell",
    "internal": "intern",
    "external": "extern"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Arbeit.csv")
