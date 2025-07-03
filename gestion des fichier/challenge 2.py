import os

chemin_dossier = "chemin_dossier"

nom_fichier = "config.yaml"

chemin_fichier = os.path.join(chemin_dossier, nom_fichier)

if os.path.exists(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print("Contenu du fichier config.yaml:\n")
else:
    print("Le fichier config.yaml n'existe pas.")