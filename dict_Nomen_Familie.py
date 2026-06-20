import pandas as pd

words = {
    "the family": "die Familie",
    "the mother": "die Mutter",
    "the father": "der Vater",
    "the parent": "der Elternteil",
    "the parents": "die Eltern",
    "the child": "das Kind",
    "the daughter": "die Tochter",
    "the son": "der Sohn",
    "the sister": "die Schwester",
    "the brother": "der Bruder",
    "the sibling": "das Geschwister",
    "the grandmother": "die Großmutter",
    "the grandfather": "der Großvater",
    "the grandparents": "die Großeltern",
    "the aunt": "die Tante",
    "the uncle": "der Onkel",
    "the cousin": "der Cousin",
    "the niece": "die Nichte",
    "the nephew": "der Neffe",
    "the wife": "die Ehefrau",
    "the husband": "der Ehemann",
    "the partner": "der Partner",
    "the marriage": "die Ehe",
    "the wedding": "die Hochzeit",
    "the baby": "das Baby",
    "the toddler": "das Kleinkind",
    "the teenager": "der Jugendliche",
    "the adult": "der Erwachsene",
    "the relative": "der Verwandte",
    "the relationship": "die Beziehung",
    "the household": "der Haushalt",
    "the birthday": "der Geburtstag",
    "the celebration": "die Feier",
    "the visit": "der Besuch",
    "the childhood": "die Kindheit",
    "the name": "der Name",
    "the age": "das Alter",
    "the home": "das Zuhause",
    "the pet": "das Haustier",
    "the generation": "die Generation"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("dict_Nomen_Familie.csv")
