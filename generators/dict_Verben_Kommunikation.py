import pandas as pd

words = {
    'to speak': 'sprechen',
    'to say': 'sagen',
    'to ask': 'fragen',
    'to answer': 'antworten',
    'to explain': 'erklären',
    'to repeat': 'wiederholen',
    'to translate': 'übersetzen',
    'to understand': 'verstehen',
    'to misunderstand': 'missverstehen',
    'to listen': 'zuhören',
    'to discuss': 'diskutieren',
    'to agree': 'zustimmen',
    'to disagree': 'widersprechen',
    'to write': 'schreiben',
    'to read': 'lesen',
    'to call': 'anrufen',
    'to send': 'schicken',
    'to receive': 'empfangen',
    'to pronounce': 'aussprechen',
    'to spell': 'buchstabieren'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Kommunikation.csv")
