students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

nom = input("Entrez le nom d'un étudiant : ")
if nom in students:
    infos = students[nom]
    print(f"Note de {nom}: ")
    for matiere, note in infos.items():
        somme_notes = 0
        nombre_notes = 0
        print(f"{matiere} note: {note}")
        somme_notes += note
        nombre_notes += 1


    moyenne = somme_notes / nombre_notes
    print(f"Moyenne de {nom}: {moyenne}")

else:
    print(f"L'étudiant {nom} n'existe pas dans la liste.")



