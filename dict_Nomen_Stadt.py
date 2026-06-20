import pandas as pd

words = {
    "the city": "die Stadt",
    "the town": "die Kleinstadt",
    "the village": "das Dorf",
    "the street": "die Straße",
    "the square": "der Platz",
    "the intersection": "die Kreuzung",
    "the traffic light": "die Ampel",
    "the sidewalk": "der Gehweg",
    "the bridge": "die Brücke",
    "the station": "der Bahnhof",
    "the bus stop": "die Bushaltestelle",
    "the subway": "die U-Bahn",
    "the tram": "die Straßenbahn",
    "the train": "der Zug",
    "the bus": "der Bus",
    "the taxi": "das Taxi",
    "the car": "das Auto",
    "the bicycle": "das Fahrrad",
    "the parking lot": "der Parkplatz",
    "the park": "der Park",
    "the playground": "der Spielplatz",
    "the market": "der Markt",
    "the supermarket": "der Supermarkt",
    "the bakery": "die Bäckerei",
    "the pharmacy": "die Apotheke",
    "the hospital": "das Krankenhaus",
    "the doctor office": "die Arztpraxis",
    "the school": "die Schule",
    "the university": "die Universität",
    "the library": "die Bibliothek",
    "the museum": "das Museum",
    "the theater": "das Theater",
    "the cinema": "das Kino",
    "the restaurant": "das Restaurant",
    "the cafe": "das Café",
    "the hotel": "das Hotel",
    "the bank": "die Bank",
    "the post office": "die Post",
    "the police station": "die Polizeiwache",
    "the city hall": "das Rathaus"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("dict_Nomen_Stadt.csv")
