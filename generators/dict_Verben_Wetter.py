import pandas as pd

words = {
    'to rain': 'regnen',
    'to snow': 'schneien',
    'to shine': 'scheinen',
    'to storm': 'stürmen',
    'to freeze': 'frieren',
    'to thaw': 'tauen',
    'to get warmer': 'wärmer werden',
    'to get colder': 'kälter werden',
    'to forecast': 'vorhersagen',
    'to change': 'sich ändern',
    'to clear up': 'aufklaren',
    'to cover': 'bedecken',
    'to blow': 'wehen',
    'to thunder': 'donnern',
    'to flash': 'blitzen',
    'to drip': 'tropfen',
    'to melt': 'schmelzen',
    'to protect': 'schützen',
    'to get wet': 'nass werden',
    'to dry': 'trocknen',
    'to hail': 'hageln',
    'to cool down': 'abkühlen',
    'to warm up': 'sich erwärmen'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Wetter.csv")
