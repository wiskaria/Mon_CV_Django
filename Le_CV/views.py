
from django.shortcuts import render

import json

with open ("info_perso.json","r") as info_perso:
        info =json.load(info_perso)



def index (request):
        context =   {'prenom':info["prenom"], 'nom':info["nom"],"numero":info["num_phone"],"email":info["email"],"adresse":info["rue"]}
        return render(request, "Le_CV/index.html",context)
    