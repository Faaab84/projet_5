
words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

liste_resultat = []


for mot in words:
    num_voy = 0
    for lettre in mot:
        if lettre in 'aeiouy':
            num_voy += 1
    tuple_mot = (mot, num_voy)
    liste_resultat.append(tuple_mot)

print(liste_resultat)
