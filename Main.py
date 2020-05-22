import json
import requests


with open("api_key.txt", "r") as f:
    lines = f.readlines()
    key = lines[0].strip()


def rename(phrase):
    if phrase == "shotgun":
        phrase = "cookie shotgun"
    
    lst = phrase.split(" ")

    fixed = []
    for w in lst:
        if w != "of":
            fixed.append(w.capitalize())
        else:
            fixed.append(w)


    return " ".join(fixed)


def skills(player):
    data = requests.get("https://api.hypixel.net/player?key={}&name={}"
            .format(key, player)).json()

    if data["player"] is None:
        return [None] * 4

    info = data["player"]["stats"]["Arena"]

    keys = ["offensive", "utility", "support", "ultimate"]
    
    setup = []
    for k in keys:
        setup.append(rename(info[k].replace("_", " ")))

    return setup


while True:
    player = input()

    if player == "q":
        break

    setup = skills(player)

    print()
    if setup[0] is None:
        print("Invalid player")
    else:
        print("{}: {}, {}, {}, {}".format(player, setup[0], setup[1], setup[2], setup[3]))
    print()