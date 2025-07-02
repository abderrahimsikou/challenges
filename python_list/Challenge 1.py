notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

moyen = sum(notes) / len(notes)

sup = [note for note in notes if note > moyen]

print(f'la moyenne:{moyen:.2f}, {sup}')
