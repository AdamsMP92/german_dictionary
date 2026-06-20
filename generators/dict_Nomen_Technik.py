import pandas as pd

words = {
    'the technology': 'die Technik',
    'the device': 'das Gerät',
    'the computer': 'der Computer',
    'the laptop': 'der Laptop',
    'the phone': 'das Handy',
    'the tablet': 'das Tablet',
    'the screen': 'der Bildschirm',
    'the keyboard': 'die Tastatur',
    'the mouse': 'die Maus',
    'the cable': 'das Kabel',
    'the battery': 'der Akku',
    'the charger': 'das Ladegerät',
    'the software': 'die Software',
    'the program': 'das Programm',
    'the file': 'die Datei',
    'the folder': 'der Ordner',
    'the password': 'das Passwort',
    'the network': 'das Netzwerk',
    'the printer': 'der Drucker',
    'the update': 'das Update'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Technik.csv")
