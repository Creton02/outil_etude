"""
Retrouvez tous les fonctions ici
"""
import pandas as pd
import os
import json
import atexit
import random as rd
import colorama as cl


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
            

    def ecraser_cote(self):
        with open(self.save_file, "w") as file:
            file.write("{}")
        print(f"{cl.Back.RED}La sauvegarde à été écrasé!{cl.Back.RESET}")
        self.cote = self.matiere.cote.tolist()


    def poser_question(self, index:int):
        print(f"<-------->")
        print(f"{self.matiere.loc[index, "terme"]}")
        input(f"  <---->")
        print(f"{self.matiere.loc[index, "definition"]}")
        input(f"   <-->")
        condition_sortie = False
        while condition_sortie == False:
            try:
                difficulte = int(input(f"Facile (1), modéré (2), difficile (3), sortir (4) "))
            except ValueError:
                difficulte = 3
            condition_sortie = True
        if self.matiere.loc[index, "detail"] != '""':
            try:
                choix = int(input(f"Plus de détail? (1) "))
            except ValueError:
                choix = 0
            if choix == 1:
                print(f"{self.matiere.loc[index, "detail"]}")
        if self.matiere.loc[index, "exemple"] != '""':
            try:
                choix = int(input(f"Un exemple? (1) "))
            except ValueError:
                choix = 2
            if choix == 1:
                print(f"{self.matiere.loc[index, "exemple"]}")
        return difficulte


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


    def reviser_matiere(self, chapitre:int):
        numero_revise = []
        chapitre_df = self.matiereetude.matiere[self.matiereetude.matiere["chapitre"] == chapitre]
        first_index = (self.matiereetude.matiere["chapitre"] == chapitre).idxmax()
        for e in range(first_index, first_index + len(chapitre_df)):
            if self.matiereetude.cote[e] == 0:
                cote = self.matiereetude.poser_question(e)
                match cote:
                    case 1:
                        self.matiereetude.cote[e] = 2
                    case 2:
                        self.matiereetude.cote[e] = 1
                    case 3:
                        self.matiereetude.cote[e] = 0
                if cote == 4:
                    self.matiereetude.save_cote()
                    break
            elif self.matiereetude.cote[e] == 1:
                random = rd.randint(1, 2)
                if random == 1:
                    cote = self.matiereetude.poser_question(e)
                    match cote:
                        case 1:
                            self.matiereetude.cote[e] = 2
                        case 2:
                            self.matiereetude.cote[e] = 1
                        case 3:
                            self.matiereetude.cote[e] = 0
                    if cote == 4:
                        self.matiereetude.save_cote()
                        break
            self.matiereetude.save_cote()


    def menu_principal(self):
        condition_sortie = False
        while condition_sortie == False:
            print(f"----------- Outil de révision -----------")
            print(f" 1 - Afficher les matières\n 2 - Ajouter une matière\n 3 - Réviser une matière")
            print(f" 4 - Écraser une sauvegarde\n 5 - Sortir")
            try:
                choix = int(input(f"Action: "))
            except ValueError:
                print(cl.Back.RED + "Valeur invalide." + cl.Back.RESET)
                choix = 0
            match choix:
                case 1:
                    pass
                case 2:
                    self.affichage_matiere()
                case 3:
                    print(self.matiereetude.matiere["chapitre"].unique())
                    try:
                        chapitre = int(input(f"Quel chapitre? "))
                    except ValueError:
                        print(f"Chapitre inexistant.")
                        break
                    self.reviser_matiere(chapitre)
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