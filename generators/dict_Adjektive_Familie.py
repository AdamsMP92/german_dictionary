import pandas as pd

words = {
    "young": "jung",
    "old": "alt",
    "older": "älter",
    "younger": "jünger",
    "married": "verheiratet",
    "single": "ledig",
    "divorced": "geschieden",
    "pregnant": "schwanger",
    "related": "verwandt",
    "close": "nah",
    "distant": "entfernt",
    "loving": "liebevoll",
    "strict": "streng",
    "patient": "geduldig",
    "impatient": "ungeduldig",
    "proud": "stolz",
    "worried": "besorgt",
    "happy": "glücklich",
    "sad": "traurig",
    "angry": "wütend",
    "calm": "ruhig",
    "loud": "laut",
    "quiet": "leise",
    "friendly": "freundlich",
    "helpful": "hilfsbereit",
    "careful": "vorsichtig",
    "responsible": "verantwortungsbewusst",
    "independent": "selbstständig",
    "dependent": "abhängig",
    "healthy": "gesund",
    "sick": "krank",
    "tired": "müde",
    "awake": "wach",
    "busy": "beschäftigt",
    "lonely": "einsam",
    "together": "zusammen",
    "private": "privat",
    "personal": "persönlich",
    "traditional": "traditionell",
    "modern": "modern"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Familie.csv")
