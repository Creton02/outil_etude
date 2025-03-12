"""
Retrouvez tous les fonctions ici
"""
import pandas as pd
import os
import json
import atexit
import random as rd

def load_excel(folder_name:str):
    path = "/workspaces/outil_etude/excel/" + folder_name + ".xlsx"
    matiere = pd.read_excel(path)
    return matiere


class MatiereEtude():
    def __init__(self, matiere:str):
        self.matiere = load_excel(matiere)
        self.save_file = "/workspaces/outil_etude/saves/" + matiere + ".json"
        if not os.path.exists(self.save_file) or os.stat(self.save_file).st_size == 0:
            print(f"Aucun fichier de  sauvegarde trouvé, création d'une nouvelle sauvegarde.")
            with open(self.save_file, "w") as file:
                json.dump(self.matiere.cote.tolist(), file, indent=4)
            self.cote = self.matiere.cote.tolist()
        else:
            with open(self.save_file, "r") as file:
                self.cote = json.load(file)
        print(f"Chargement de la sauvegarde.")


    def save_cote(self):
        with open(self.save_file, "w") as file:
            json.dump(self.cote, file, indent=4)
            

    def ecraser_cote(self):#à retravailler
        with open(self.save_file, "w") as file:
            file.write("{}")
        print(f"La sauvegarde à été écrasé!")
        self.cote = self.matiere.cote.tolist()


    def poser_question(self, index:int):
        print(f"{self.matiere.loc[index, "terme"]}")
        input(f"      ---------       ")
        print(f"{self.matiere.loc[index, "definition"]}")
        input(f"      ---------       ")
        difficulte = 0
        while difficulte not in range(1, 4):
            try:
                difficulte = int(input(f"Facile (1), modéré (2), difficile (3) "))
            except ValueError:
                difficulte = 3
            match difficulte:
                case "1":
                    self.cote[index] = 2
                case "2":
                    self.cote[index] = 1
                case "3":
                    self.cote[index] = 0
        if self.matiere.loc[index, "detail"] != '""':
            try:
                choix = int(input(f"Plus de détail? (1) "))
            except ValueError:
                choix = 0
            if choix == 1:
                print(f"{self.matiere.loc[index, "detail"]}")
        if self.matiere.loc[index, "exemple"] != '"':
            try:
                choix = int(input(f"Un exemple? (1) "))
            except ValueError:
                choix = 2
            if choix == 1:
                print(f"{self.matiere.loc[index, "exemple"]}")
    def __str__(self):
        affichage = ""
        for e in range(len(self.matiere)):
            affichage += self.matiere.loc[e, "terme"]
            affichage += "\n"
        return(affichage)
    
    
class Menu():
    def __init__(self, paths:list):
        self.paths = paths
        self.matiereetude = MatiereEtude("feuille_note_biologie")
        atexit.register(self.matiereetude.save_cote)

    def affichage_matiere(self):
        pass


    def reviser_matiere(self):
        numero_revise = []
        for e in range(len(self.matiereetude.matiere.cote)):
            if self.matiereetude.matiere.cote[e] == 0:
                self.matiereetude.poser_question(e)
            elif self.matiereetude.matiere.cote[e] == 1:
                random = rd.randint(2)
                if random == 1:
                    self.matiereetude.poser_question(e)

        self.matiereetude.poser_question(2)


    def menu_principal(self):
        condition_sortie = False
        while condition_sortie == False:
            print(f"----------- Outil de révision -----------")
            print(f" 1 - Consulter les différentes matières\n 2 - Afficher une matière\n 3 - Réviser une matière")
            print(f" 4 - Écraser une sauvegarde\n 5 - Sortir")
            choix = int(input(f"Action: "))
            
            match choix:
                case 1:
                    pass
                case 2:
                    self.affichage_matiere
                case 3:
                    self.reviser_matiere()
                case 4:
                    self.matiereetude.ecraser_cote()
                case 5:
                    condition_sortie = True
        


    def __str__(self):
        return "ceci est l'affichage du menu"

    
def main():
    
    liste_paths = ["feuille_note_biologie"]
    menu = Menu(liste_paths)
    menu.menu_principal()
    """biologie = MatiereEtude("feuille_note_biologie")
    atexit.register(biologie.save_cote)
    biologie.poser_question(2)
    biologie.ecraser_cote"""
    
if __name__ == "__main__":
    main()