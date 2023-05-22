import os
import json
import pandas as pd

def parse_cv(cv_text):
    cv = json.loads(cv_text)

    info_basique = cv["info_basique"]
    nom_complet = info_basique["nom_complet"]
    email = info_basique["email"]
    linkedin_url = info_basique["linkedin_url"]
    niveau_education = info_basique["niveau_education"]
    université = info_basique["université"]
    annee_de_diplomation = info_basique["annee_de_diplomation"]

    experiences = cv["experience_professionnelle"]
    postes = []
    for i in range(5):  # Nous allons itérer 5 fois, car nous avons au maximum 5 expériences
        if i < len(experiences):
            exp = experiences[i]
            titre_du_poste = exp["titre_du_poste"]
            entreprise = exp["entreprise"]
            durée = exp["durée"]
            postes.extend([titre_du_poste, entreprise, durée])
        else:
            postes.extend([None, None, None])  # Si nous n'avons pas d'expérience à cet indice, nous ajoutons None pour les trois valeurs

    return [nom_complet, email, linkedin_url, niveau_education, université, annee_de_diplomation, *postes]

data = []

directory = 'CV_parsed'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), 'r') as file:
            cv_text = file.read()
            filename_without_extension = os.path.splitext(filename)[0]
            data.append([filename_without_extension] + parse_cv(cv_text))  # Nous ajoutons le nom du fichier au début de chaque ligne

df = pd.DataFrame(data, columns=["nom_fichier", "nom_complet", "email", "linkedin_url", "niveau_education", "université", "annee_de_diplomation", 
                                 "poste 1", "entreprise 1", "durée 1", 
                                 "poste 2", "entreprise 2", "durée 2", 
                                 "poste 3", "entreprise 3", "durée 3", 
                                 "poste 4", "entreprise 4", "durée 4", 
                                 "poste 5", "entreprise 5", "durée 5"])

print(os.getcwd())
df.to_excel("cvs.xlsx", index=False)

