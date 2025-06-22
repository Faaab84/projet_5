def calculate_average(numbers):
    total = sum(numbers)
    length = len(numbers)
    return total / length


if __name__ == '__main__':

    numbers = [10, 20, 30, 40, 50]

    average = calculate_average(numbers)
    print("La moyenne est :", average)
