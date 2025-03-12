"""
Retrouvez tous les fonctions ici
"""
import pandas as pd
import os

def load_excel(folder_name:str):
    path = "/workspaces/outil_etude/excel/" + folder_name + ".xlsx"
    matiere = pd.read_excel(path)
    return matiere

class MatiereEtude():
    def __init__(self, matiere:str):
        self.matiere = load_excel(matiere)
        save_file = "/workspaces/outil_etude/saves/" + matiere + ".json"
        if not os.path.exists(save_file) or os.stat(save_file).st_size == 0:
            print(f"Aucun fichier de  sauvegarde trouvé, création d'une nouvelle sauvegarde.")
            with open(save_file, "w") as file:
                json.dump(self.matiere.cote, file, indent=4)
            self.cote = self.matiere.cote
        else:
            with open(save_file, "r") as file:
                self.cote = json.load(file)
        print(f"Chargement de la sauvegarde.")


    def poser_question(self, index:int):
        print(f"{self.matiere.loc[index, "terme"]}")
        input(f"      ---------       ")
        print(f"{self.matiere.loc[index, "definition"]}")
        input(f"      ---------       ")
        difficulte = 0
        while difficulte is not in range(1, 4):
            difficulte = int(input(f"Facile (1), modéré (2), difficile (3)"))
            match difficulte:
                case 1:
                    self.cote.loc[index] = 2
                case 2:
                    self.cote.loc[index] = 1
                case 3:
                    self.cote.loc[index] = 0
        if self.matiere.loc[index, "detail"] != '""':
            choix = int(input(f"(1)"))
            if choix == 1:
                print(f"{self.matiere.loc[index, "detail"]}")
        
    def __str__(self):
        affichage = ""
        for e in range(len(self.matiere)):
            affichage += self.matiere.loc[e, "terme"]
            affichage += "\n"
        return(affichage)
    
    
class Menu():
    def __init__(self, paths:list, matiereetude:class):
        self.paths = paths
        self.matiereetude = MatiereEtude("feuille_note_biologie")
    

    def menu_principal(self):
        print(f"----------- Outil de révision -----------")
        print(f" 1 - Consulter les différentes matières\n 2 - Afficher une matière\n 3 - Réviser une matière")


    def affichage_matiere(self):
        pass


    def reviser_matiere(self):
        pass


    def __str__(self):
        return "ceci est l'affichage du menu"

    
def main():
    liste_paths = ["feuille_note_biologie"]
    biologie = MatiereEtude("feuille_note_biologie")
    
    biologie.afficher_terme(2)
    biologie.afficher_definition(2)
    

if __name__ == "__main__":
    main()