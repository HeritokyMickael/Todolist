import customtkinter as ctk
from form_tache import inscription
from gestion_check import *

class ToDoListView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To Do List")
        self.geometry("600x400")

        Titre = ctk.CTkLabel(self, text="TO DO LIST", font=("Arial", 40, "bold"))
        Titre.pack(side="top", pady=20)

        self.Section = ctk.CTkFrame(self, fg_color="green")
        self.Section.pack(expand=True)

        affichage_Tire = ctk.CTkLabel(self.Section, text="Titre dans le fichier json")

        btn_ajouter = ctk.CTkButton(self.Section, text="Ajouter", command = lambda :inscription(self))
        btn_ajouter.pack(expand=True)

        self.affichage()

    def affichage (self):

        liste_des_taches = charge_checklist()

        if not liste_des_taches:
            message = ctk.CTkLabel(self.Section, text="il n'y a aucun tache")
            message.pack(pady = 10)
        else : 
            for tache , details in liste_des_taches.items():
                self.template(tache, details)
        
    def template (self, tache, details):
        cadre = ctk.CTkFrame(self.Section, corner_radius=10)
        cadre.pack(fill="y")

        affiche_titre = ctk.CTkLabel(cadre, text = f"Titre : {tache}")
        affiche_titre.pack(side="top", anchor="w")
        affiche_Duree = ctk.CTkLabel(cadre, text = f"Durée : {details['heure']}h {details['minute']} min")
        affiche_Duree.pack(side="top", anchor="w")
        affiche_materiel = ctk.CTkLabel(cadre, text = f"Materiel : {details['materiel']}")
        affiche_materiel.pack(side="top", anchor="w")
        affiche_responsable = ctk.CTkLabel(cadre, text = f"Responsable : {details['responsable']}")
        affiche_responsable.pack(side="top", anchor="w")
        affiche_description = ctk.CTkLabel(cadre, text = f"Description : {details['description']}")
        affiche_description.pack(side="top", anchor="w")




    


       
        #recuperation des donnes a afficher
       

app = ToDoListView()
app.mainloop()
