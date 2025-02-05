
import json

NomDuFichier = "checlist.json"

def charge_checklist ():
    try:
        with open (NomDuFichier, "r") as Fichier :
            return json.load(Fichier)
    except FileNotFoundError : 
        return {}
    except json.JSONDecodeError :
        return {}

def sauve_checklist (donnee):
    with open (NomDuFichier,"w") as Fichier :
        json.dump (donnee, Fichier , indent= 4)

def Ajouter_checklist(cle, valeur):
    donnee = charge_checklist()
    if donnee is None:
        donnee = {}
    donnee[cle] = valeur
    sauve_checklist(donnee)
