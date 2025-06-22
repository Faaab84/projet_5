def log_decorator(func):
    def wrapper():
        print("Début de l'exécution de la fonction.")
        func()
        print("Fin de l'exécution de la fonction.")
    return wrapper

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


if __name__ == '__main__':
    function_test()

