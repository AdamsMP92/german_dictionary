import pandas as pd

words = {
    'the media': 'die Medien',
    'the newspaper': 'die Zeitung',
    'the magazine': 'die Zeitschrift',
    'the article': 'der Artikel',
    'the news': 'die Nachrichten',
    'the website': 'die Webseite',
    'the podcast': 'der Podcast',
    'the video': 'das Video',
    'the channel': 'der Kanal',
    'the post': 'der Beitrag',
    'the comment': 'der Kommentar',
    'the photo': 'das Foto',
    'the headline': 'die Überschrift',
    'the report': 'der Bericht',
    'the interview': 'das Interview',
    'the advertisement': 'die Werbung',
    'the source': 'die Quelle',
    'the screen': 'der Bildschirm',
    'the app': 'die App',
    'the profile': 'das Profil'
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("../csv-files/dict_Nomen_Medien.csv")
