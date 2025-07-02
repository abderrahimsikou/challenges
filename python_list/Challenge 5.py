def compterOccurrences(x, y):
    compteur = 0
    for element in y:
        if element == x:
            compteur += 1
    return compteur

liste = [7, 24, 5, 23, 7, 22, 23, 12, 29]
print(compterOccurrences(24, liste)) 
print(compterOccurrences(7, liste)) 
print(compterOccurrences(99, liste)) 