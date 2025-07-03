First_dict = { "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" } 

First_dict['RAM'] = '32G'

print(First_dict.keys())
print(First_dict.values())

print(First_dict.items())

First_dict['Système d’exploitation'] = 'Windows 10'

for x, y in First_dict.items():
    print(x,y)

new = First_dict["Processeur"], First_dict["Carte Graphique"] = First_dict["Carte Graphique"],First_dict["Processeur"]
new = First_dict["Intel core i7-G11"], First_dict["GeForce RTX 3070"] = First_dict["GeForce RTX 3070"],First_dict["Intel core i7-G11"]

