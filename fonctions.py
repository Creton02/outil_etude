"""
Retrouvez tous les fonctions ici
"""
import pandas as pd

def load_excel(folder_name:str):
    path = "/workspaces/outil_etude/excel/" + folder_name
    matiere = pd.read_excel(path)
    return matiere

class MatiereEtude():
    def __init__(self, matiere):
        self.matiere = load_excel(matiere)


    def afficher_terme(self, index:int):
        print(f"{self.matiere.loc[index, "terme"]}")


    def afficher_definition(self, index:int):
        print(f"{self.matiere.loc[index, "definition"]}")
        if self.matiere.loc[index, "detail"] != '""':
            choix = int(input(f"Voulez vous en savoir plus? (1)"))
            if choix == 1:
                print(f"{self.matiere.loc[index, "detail"]}")
        
    def __str__(self):
        affichage = ""
        for e in range(len(self.matiere)):
            affichage += self.matiere.loc[e, "terme"]
            affichage += "\n"
        return(affichage)
    

class Question():
    def __init__(self):
        pass


    def poser_question(self):
        pass

    
    def actualiser_cote(self):
        pass


    def __str__(self):
        return("print de question")
    


def main():
    biologie = MatiereEtude("feuille_note_biologie.xlsx")
    
    biologie.afficher_terme(2)
    biologie.afficher_definition(2)


if __name__ == "__main__":
    main()