import pandas as pd

words = {
    'the authority': 'die Behörde',
    'the office': 'das Amt',
    'the citizen': 'der Bürger',
    'the form': 'das Formular',
    'the application': 'der Antrag',
    'the document': 'das Dokument',
    'the passport': 'der Reisepass',
    'the identity card': 'der Personalausweis',
    'the residence permit': 'die Aufenthaltserlaubnis',
    'the registration': 'die Anmeldung',
    'the appointment': 'der Termin',
    'the counter': 'der Schalter',
    'the number': 'die Nummer',
    'the signature': 'die Unterschrift',
    'the certificate': 'die Bescheinigung',
    'the copy': 'die Kopie',
    'the fee': 'die Gebühr',
    'the deadline': 'die Frist',
    'the notice': 'der Bescheid',
    'the tax office': 'das Finanzamt'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Behoerden.csv")
