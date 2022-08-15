import json

with open ("info_perso.json","r") as info_perso:
        info =json.load(info_perso)
        print(info)

