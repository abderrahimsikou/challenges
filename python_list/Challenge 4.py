def rechercheElement(x, liste):
    for i in range(len(liste)):
        if liste[i] == x:
            return i
    return False
liste = [5, 10, 15, 20, 25, 30]
print(rechercheElement(15, liste))
print(rechercheElement(40, liste))