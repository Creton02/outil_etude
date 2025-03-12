"""
Retrouvez tous les fonctions ici
"""
import pandas as pd

def load_excel(folder_name:str):
    path = "excel_files/" + folder_name
    matiere = pd.read_excel(path)
    return matiere

class MatiereEtude():
    def __init__(self, matiere):
        self.chapitre = matiere[""]


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
    pass


if __name__ == "__main__":
    main()
