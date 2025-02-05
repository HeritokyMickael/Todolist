import customtkinter as ctk
import tkinter as tk
from gestion_check import Ajouter_checklist

def inscription(self):
    formulaire = ctk.CTkToplevel(self)
    formulaire.title("Ajouter un Thème")
    formulaire.geometry("400x300")


    frame_formulaire = ctk.CTkFrame(formulaire)
    frame_formulaire.pack(fill="both", expand=True, padx=10, pady=10)

 
    label_Titre = ctk.CTkLabel(frame_formulaire, text="Titre: ")
    label_Titre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    saisi_Titre = ctk.CTkEntry(frame_formulaire , placeholder_text="Titre du tâche")
    saisi_Titre.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    label_heure = ctk.CTkLabel(frame_formulaire, text="Durée: ")
    label_heure.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    saisi_heure = tk.Spinbox(frame_formulaire , from_= 0, to = 12 , width= 2)
    saisi_minute = tk.Spinbox(frame_formulaire , from_= 0, to = 60 , width= 2)
    saisi_heure.grid(row=1, column=1, padx=2, pady=5)
    saisi_minute.grid(row=1, column=2, padx=2, pady=5, sticky="ew")

    label_Materiel_a_utiliser = ctk.CTkLabel(frame_formulaire, text="Matériel nécessaire: ")
    label_Materiel_a_utiliser.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    text_materiel = ctk.CTkTextbox(frame_formulaire,  height=4)
    text_materiel.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    label_responsable = ctk.CTkLabel(frame_formulaire, text="Responsable: ")
    label_responsable.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    text_responsable = ctk.CTkTextbox(frame_formulaire, height=4 )
    text_responsable.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    label_description = ctk.CTkLabel(frame_formulaire, text="Description: ")
    label_description.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    text_description = ctk.CTkTextbox(frame_formulaire, height=4)
    text_description.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    btn_enregistrer = ctk.CTkButton(formulaire, text="Enregistrer", command= lambda :recuperation_des_donnes())
    btn_enregistrer.pack(pady=10)
    btn_fermer = ctk.CTkButton(formulaire, text="Fermer", command=formulaire.destroy)
    btn_fermer.pack()

   
    frame_formulaire.grid_columnconfigure(1, weight=1)
    
    #recuperation des donnees 

    def recuperation_des_donnes():
        titre = saisi_Titre.get()
        heure = saisi_heure.get()
        minute = saisi_minute.get()
        materiel = text_materiel.get("1.0","end").strip()
        responsable = text_responsable.get("1.0","end").strip()
        description = text_description.get("1.0","end").strip()
    #test_sur les donnes recuperer

        les_taches = {
            "heure" : heure,
            "minute": minute,
            "materiel" : materiel,
            "responsable" : responsable,
            "description" : description
        }
        Ajouter_checklist(titre, les_taches)
        print(titre)
        