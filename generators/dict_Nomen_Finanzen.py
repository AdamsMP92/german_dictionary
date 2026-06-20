import pandas as pd

words = {
    'the money': 'das Geld',
    'the bank': 'die Bank',
    'the account': 'das Konto',
    'the card': 'die Karte',
    'the credit card': 'die Kreditkarte',
    'the cash': 'das Bargeld',
    'the coin': 'die Münze',
    'the bill': 'der Geldschein',
    'the price': 'der Preis',
    'the cost': 'die Kosten',
    'the invoice': 'die Rechnung',
    'the receipt': 'der Beleg',
    'the salary': 'das Gehalt',
    'the rent': 'die Miete',
    'the tax': 'die Steuer',
    'the debt': 'die Schulden',
    'the savings': 'die Ersparnisse',
    'the transfer': 'die Überweisung',
    'the loan': 'der Kredit',
    'the insurance': 'die Versicherung'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Finanzen.csv")
