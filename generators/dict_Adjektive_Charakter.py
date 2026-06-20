import pandas as pd

words = {
    'friendly': 'freundlich',
    'honest': 'ehrlich',
    'patient': 'geduldig',
    'impatient': 'ungeduldig',
    'brave': 'mutig',
    'shy': 'schüchtern',
    'confident': 'selbstbewusst',
    'curious': 'neugierig',
    'creative': 'kreativ',
    'reliable': 'zuverlässig',
    'lazy': 'faul',
    'hard-working': 'fleißig',
    'polite': 'höflich',
    'rude': 'unhöflich',
    'generous': 'großzügig',
    'selfish': 'egoistisch',
    'calm': 'ruhig',
    'nervous': 'nervös',
    'optimistic': 'optimistisch',
    'pessimistic': 'pessimistisch'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Charakter.csv")
