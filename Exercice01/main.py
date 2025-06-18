

def print_bonjour(nom, age):
    print(f"Bonjour, je m'appelle {nom} et j'ai {age} ans.")


if __name__ == '__main__':

    nom = input("Entrez votre nom : ")
    age = int(input("Entrez votre âge : "))

    print_bonjour(nom, age)
