notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }

etudiantAdmis = {}
etudiantNonAdmis = {}

for x, y in notes_eleves.items():
    if y >= 10:
        etudiantAdmis[x] = y 
    else:
        etudiantNonAdmis[x] = y


print(etudiantAdmis)
print('===================================')
print(etudiantNonAdmis)
        