import pandas as pd

words = {
    'the time': 'die Zeit',
    'the day': 'der Tag',
    'the week': 'die Woche',
    'the month': 'der Monat',
    'the year': 'das Jahr',
    'the hour': 'die Stunde',
    'the minute': 'die Minute',
    'the second': 'die Sekunde',
    'the morning': 'der Morgen',
    'the noon': 'der Mittag',
    'the evening': 'der Abend',
    'the night': 'die Nacht',
    'the past': 'die Vergangenheit',
    'the present': 'die Gegenwart',
    'the future': 'die Zukunft',
    'the moment': 'der Moment',
    'the appointment': 'der Termin',
    'the deadline': 'die Frist',
    'the calendar': 'der Kalender',
    'the schedule': 'der Zeitplan'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Zeit.csv")
