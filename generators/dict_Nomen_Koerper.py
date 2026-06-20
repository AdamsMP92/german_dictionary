import pandas as pd

words = {
    'the body': 'der Körper',
    'the head': 'der Kopf',
    'the face': 'das Gesicht',
    'the eye': 'das Auge',
    'the ear': 'das Ohr',
    'the nose': 'die Nase',
    'the mouth': 'der Mund',
    'the tooth': 'der Zahn',
    'the tongue': 'die Zunge',
    'the neck': 'der Hals',
    'the shoulder': 'die Schulter',
    'the arm': 'der Arm',
    'the elbow': 'der Ellbogen',
    'the hand': 'die Hand',
    'the finger': 'der Finger',
    'the chest': 'die Brust',
    'the back': 'der Rücken',
    'the stomach': 'der Bauch',
    'the leg': 'das Bein',
    'the knee': 'das Knie'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Koerper.csv")
