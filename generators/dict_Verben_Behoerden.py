import pandas as pd

words = {
    'to apply for': 'beantragen',
    'to register': 'anmelden',
    'to deregister': 'abmelden',
    'to fill out': 'ausfüllen',
    'to submit': 'einreichen',
    'to sign': 'unterschreiben',
    'to copy': 'kopieren',
    'to certify': 'beglaubigen',
    'to approve': 'genehmigen',
    'to reject': 'ablehnen',
    'to wait': 'warten',
    'to call': 'anrufen',
    'to clarify': 'klären',
    'to prove': 'nachweisen',
    'to pay': 'bezahlen',
    'to extend': 'verlängern',
    'to renew': 'erneuern',
    'to process': 'bearbeiten',
    'to receive': 'erhalten',
    'to complain': 'sich beschweren'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Behoerden.csv")
