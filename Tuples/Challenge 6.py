etudiant_info = ('yassmine',  22, 'Informatique', 17.4)

# Affiche les informations stockées dans le tuple
print(etudiant_info)
print('Prenom:' , etudiant_info[0])
print('Age:' , etudiant_info[1])
print('Filiere:' , etudiant_info[2])
print('Moyenne générale:' , etudiant_info[3])

#try:
#    etudiant_info[2] = 'Math'
#except TypeError as e:
#    print(e)
#   """
#    Les Tuples sont imutables dans Pyhton
#    """

# slicing pour afficher uniquement le prénom et l'âge.
print(etudiant_info[:2])

# nouveau tuple
new_tuple = ('tres bien', 2024)

combine = etudiant_info + new_tuple

for x , y in enumerate(combine, 1):
    print(x,y)
