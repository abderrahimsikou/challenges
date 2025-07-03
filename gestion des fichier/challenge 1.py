import os

chemin_dossier = "folder_path"

contenu_total = ""

for nom_fichier in os.listdir(chemin_dossier):
    if nom_fichier.endswith(".txt"):
        chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            contenu_total += contenu + "\n"