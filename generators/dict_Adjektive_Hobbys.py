import pandas as pd

words = {
    'creative': 'kreativ',
    'relaxing': 'entspannend',
    'interesting': 'interessant',
    'boring': 'langweilig',
    'fun': 'spaßig',
    'difficult': 'schwierig',
    'easy': 'einfach',
    'musical': 'musikalisch',
    'artistic': 'künstlerisch',
    'social': 'sozial',
    'quiet': 'ruhig',
    'loud': 'laut',
    'expensive': 'teuer',
    'cheap': 'günstig',
    'regular': 'regelmäßig',
    'spontaneous': 'spontan',
    'private': 'privat',
    'public': 'öffentlich',
    'useful': 'nützlich',
    'entertaining': 'unterhaltsam'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Hobbys.csv")
