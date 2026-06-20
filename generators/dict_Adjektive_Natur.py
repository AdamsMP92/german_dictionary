import pandas as pd

words = {
    'natural': 'natürlich',
    'green': 'grün',
    'wild': 'wild',
    'tame': 'zahm',
    'fresh': 'frisch',
    'clean': 'sauber',
    'dirty': 'schmutzig',
    'deep': 'tief',
    'high': 'hoch',
    'low': 'niedrig',
    'dry': 'trocken',
    'wet': 'nass',
    'quiet': 'ruhig',
    'loud': 'laut',
    'beautiful': 'schön',
    'dangerous': 'gefährlich',
    'protected': 'geschützt',
    'rare': 'selten',
    'common': 'häufig',
    'environmental': 'ökologisch'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Natur.csv")
