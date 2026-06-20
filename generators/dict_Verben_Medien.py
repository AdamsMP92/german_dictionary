import pandas as pd

words = {
    'to read': 'lesen',
    'to watch': 'anschauen',
    'to listen': 'anhören',
    'to publish': 'veröffentlichen',
    'to post': 'posten',
    'to comment': 'kommentieren',
    'to share': 'teilen',
    'to like': 'liken',
    'to follow': 'folgen',
    'to subscribe': 'abonnieren',
    'to search': 'suchen',
    'to download': 'herunterladen',
    'to upload': 'hochladen',
    'to stream': 'streamen',
    'to report': 'berichten',
    'to interview': 'interviewen',
    'to advertise': 'werben',
    'to edit': 'bearbeiten',
    'to record': 'aufnehmen',
    'to delete': 'löschen'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Verben_Medien.csv")
