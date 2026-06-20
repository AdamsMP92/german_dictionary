import pandas as pd

words = {
    'the communication': 'die Kommunikation',
    'the conversation': 'das Gespräch',
    'the question': 'die Frage',
    'the answer': 'die Antwort',
    'the message': 'die Nachricht',
    'the email': 'die E-Mail',
    'the call': 'der Anruf',
    'the letter': 'der Brief',
    'the word': 'das Wort',
    'the sentence': 'der Satz',
    'the meaning': 'die Bedeutung',
    'the opinion': 'die Meinung',
    'the argument': 'das Argument',
    'the explanation': 'die Erklärung',
    'the translation': 'die Übersetzung',
    'the language': 'die Sprache',
    'the voice': 'die Stimme',
    'the tone': 'der Ton',
    'the misunderstanding': 'das Missverständnis',
    'the agreement': 'die Zustimmung'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Kommunikation.csv")
