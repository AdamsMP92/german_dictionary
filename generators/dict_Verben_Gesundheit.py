import pandas as pd

words = {
    'to heal': 'heilen',
    'to treat': 'behandeln',
    'to examine': 'untersuchen',
    'to diagnose': 'diagnostizieren',
    'to prescribe': 'verschreiben',
    'to take medicine': 'Medikamente nehmen',
    'to hurt': 'wehtun',
    'to ache': 'schmerzen',
    'to recover': 'sich erholen',
    'to rest': 'sich ausruhen',
    'to call the doctor': 'den Arzt rufen',
    'to make an appointment': 'einen Termin machen',
    'to measure': 'messen',
    'to vaccinate': 'impfen',
    'to disinfect': 'desinfizieren',
    'to bandage': 'verbinden',
    'to cough': 'husten',
    'to sneeze': 'niesen',
    'to vomit': 'sich übergeben',
    'to faint': 'ohnmächtig werden'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Gesundheit.csv")
