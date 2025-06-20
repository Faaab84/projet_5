class MyClass:
    """Classe pour gérer un nom"""

    def __init__(self, full_name):
        """Initialise l'instance avec un nom

        Args:
            full_name (str): Le nom
        """
        self.full_name = full_name

    def display_name(self):
        """Affiche le nom"""
        print("Le nom est :", self.full_name)


class OtherClass:
    """Classe pour gérer un prénom et un nom"""

    def __init__(self, first_name, name):
        """Initialise l'instance avec un prénom et un nom

        Args:
            first_name (str): Le prénom
            name (str): Le nom
        """
        self.first_name = first_name
        self.name = name

    def display_name(self):
        """Affiche le nom complet (prénom + nom)"""
        print(f"Nom complet: {self.first_name} {self.name}")
