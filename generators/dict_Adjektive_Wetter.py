import pandas as pd

words = {
    'sunny': 'sonnig',
    'cloudy': 'bewölkt',
    'rainy': 'regnerisch',
    'snowy': 'verschneit',
    'windy': 'windig',
    'stormy': 'stürmisch',
    'foggy': 'neblig',
    'hot': 'heiß',
    'cold': 'kalt',
    'warm': 'warm',
    'cool': 'kühl',
    'dry': 'trocken',
    'wet': 'nass',
    'humid': 'feucht',
    'icy': 'eisig',
    'mild': 'mild',
    'clear': 'klar',
    'gray': 'grau',
    'fresh': 'frisch',
    'changeable': 'wechselhaft',
    'overcast': 'bedeckt',
    'frosty': 'frostig',
    'muggy': 'schwül'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Wetter.csv")
