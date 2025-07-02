name = input("Enter Name:")

name_inverse = ""

longueur = len(name) - 1

while longueur >= 0:
    name_inverse += name[longueur]
    longueur -=1

print(f"{name_inverse}")