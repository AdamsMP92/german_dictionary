import pandas as pd

words = {
    'happy': 'glücklich',
    'sad': 'traurig',
    'angry': 'wütend',
    'afraid': 'ängstlich',
    'worried': 'besorgt',
    'hopeful': 'hoffnungsvoll',
    'loving': 'liebevoll',
    'jealous': 'eifersüchtig',
    'proud': 'stolz',
    'ashamed': 'beschämt',
    'grateful': 'dankbar',
    'calm': 'ruhig',
    'nervous': 'nervös',
    'stressed': 'gestresst',
    'relaxed': 'entspannt',
    'lonely': 'einsam',
    'confident': 'zuversichtlich',
    'disappointed': 'enttäuscht',
    'surprised': 'überrascht',
    'satisfied': 'zufrieden',
    'relieved': 'erleichtert',
    'moved': 'gerührt',
    'homesick': 'heimwehkrank'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Gefuehle.csv")
