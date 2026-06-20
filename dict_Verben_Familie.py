import pandas as pd

words = {
    "to live": "leben",
    "to love": "lieben",
    "to marry": "heiraten",
    "to divorce": "sich scheiden lassen",
    "to separate": "sich trennen",
    "to be born": "geboren werden",
    "to raise": "erziehen",
    "to care for": "sich kümmern um",
    "to help": "helfen",
    "to support": "unterstützen",
    "to visit": "besuchen",
    "to invite": "einladen",
    "to celebrate": "feiern",
    "to give": "schenken",
    "to receive": "bekommen",
    "to call": "anrufen",
    "to talk": "reden",
    "to listen": "zuhören",
    "to argue": "streiten",
    "to reconcile": "sich versöhnen",
    "to remember": "sich erinnern",
    "to forget": "vergessen",
    "to miss": "vermissen",
    "to trust": "vertrauen",
    "to protect": "beschützen",
    "to accompany": "begleiten",
    "to pick up": "abholen",
    "to bring": "bringen",
    "to take care": "aufpassen",
    "to play": "spielen",
    "to learn": "lernen",
    "to teach": "beibringen",
    "to grow": "wachsen",
    "to move": "umziehen",
    "to inherit": "erben",
    "to adopt": "adoptieren",
    "to babysit": "babysitten",
    "to hug": "umarmen",
    "to kiss": "küssen",
    "to comfort": "trösten"
}

df = pd.DataFrame.from_dict(
    words,
    orient="index",
    columns=["German"]
)

df.index.name = "English"

df.to_csv("dict_Verben_Familie.csv")
