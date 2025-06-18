# Fonction calculate_average
def calculate_average(numbers):
    total = sum(numbers)
    length = len(numbers)
    return total / length


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]

average = calculate_average(numbers)
print("La moyenne est :", average)
