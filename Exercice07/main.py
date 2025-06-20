def square(nombre):
    try:
        result = float(nombre)
        return result ** 2
    except (ValueError, TypeError):
        print("Il faut écrire uniquement un nombre !")


nombre = input("Entrez un nombre : ")
square_resultat = square(nombre)
if square_resultat is not None:
    print(f"Le carré est : {square_resultat}")