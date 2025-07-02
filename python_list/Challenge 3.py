stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]

# la liste initiale
print('la liste initiale', stock)

# deux nouvelles listes
chaine  = [item for item in stock if isinstance(item, str)]
nombers = [item for item in stock if isinstance(item, int)]

chaine_trier  = sorted(chaine)
nombers_trier = sorted(nombers, reverse=True)

print('Chaines_triees:', chaine_trier)
print('Nombres_triees:', nombers_trier)