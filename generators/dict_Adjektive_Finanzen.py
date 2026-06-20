import pandas as pd

words = {
    'expensive': 'teuer',
    'cheap': 'günstig',
    'free': 'kostenlos',
    'affordable': 'bezahlbar',
    'monthly': 'monatlich',
    'annual': 'jährlich',
    'gross': 'brutto',
    'net': 'netto',
    'private': 'privat',
    'public': 'öffentlich',
    'insured': 'versichert',
    'secure': 'sicher',
    'risky': 'riskant',
    'profitable': 'rentabel',
    'financial': 'finanziell',
    'valid': 'gültig',
    'overdue': 'überfällig',
    'automatic': 'automatisch',
    'electronic': 'elektronisch',
    'cashless': 'bargeldlos'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Adjektive_Finanzen.csv")
