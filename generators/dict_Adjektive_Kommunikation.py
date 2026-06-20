import pandas as pd

words = {
    'clear': 'klar',
    'unclear': 'unklar',
    'loud': 'laut',
    'quiet': 'leise',
    'polite': 'höflich',
    'rude': 'unhöflich',
    'direct': 'direkt',
    'indirect': 'indirekt',
    'honest': 'ehrlich',
    'formal': 'formell',
    'informal': 'informell',
    'written': 'schriftlich',
    'oral': 'mündlich',
    'understandable': 'verständlich',
    'confusing': 'verwirrend',
    'important': 'wichtig',
    'short': 'kurz',
    'long': 'lang',
    'friendly': 'freundlich',
    'critical': 'kritisch'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Kommunikation.csv")
