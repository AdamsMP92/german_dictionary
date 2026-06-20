import pandas as pd

words = {
    'to pay': 'bezahlen',
    'to save': 'sparen',
    'to spend': 'ausgeben',
    'to earn': 'verdienen',
    'to transfer': 'überweisen',
    'to withdraw': 'abheben',
    'to deposit': 'einzahlen',
    'to borrow': 'leihen',
    'to lend': 'verleihen',
    'to owe': 'schulden',
    'to cost': 'kosten',
    'to calculate': 'berechnen',
    'to compare': 'vergleichen',
    'to insure': 'versichern',
    'to invest': 'investieren',
    'to cancel': 'kündigen',
    'to book': 'buchen',
    'to check': 'prüfen',
    'to donate': 'spenden',
    'to refund': 'erstatten'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Finanzen.csv")
