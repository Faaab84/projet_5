
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Le nom de la personne est: {self.name} et son age est {self.age} ans.")


class Employee(Person):

    def __init__(self, name, age, salary):

        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Son salaire est de: {self.salary} €")




employee = Employee("Paul", 12, 1320)
employee.display_details()


