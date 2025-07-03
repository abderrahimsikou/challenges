import os
import shutil

dossier_source = "folder_chemein"
dossier_destination = "chemin_destination"

os.makedirs(dossier_destination, exist_ok=True)

for fichier in os.listdir(dossier_source):
    if fichier.endswith(".csv"):
        chemin_source = os.path.join(dossier_source, fichier)
        chemin_destination = os.path.join(dossier_destination, fichier)
        shutil.copy(chemin_source, chemin_destination)