import pandas as pd

words = {
    'elegant': 'elegant',
    'casual': 'lässig',
    'formal': 'formell',
    'comfortable': 'bequem',
    'tight': 'eng',
    'loose': 'locker',
    'long': 'lang',
    'short': 'kurz',
    'warm': 'warm',
    'thin': 'dünn',
    'thick': 'dick',
    'clean': 'sauber',
    'dirty': 'schmutzig',
    'wet': 'nass',
    'dry': 'trocken',
    'fashionable': 'modisch',
    'old-fashioned': 'altmodisch',
    'colorful': 'bunt',
    'plain': 'einfarbig',
    'striped': 'gestreift'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Kleidung.csv")
