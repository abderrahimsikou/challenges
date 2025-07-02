Ch1 = "Le langage Python est très populaire"

Ch2 = "Python est un langage puissant"

mots1 = set(Ch1.split())

mots2 = set(Ch2.split())

communs = list(mots1 & mots2)

print(f'les mots communs:{communs}')