
class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        area = self.width * self.length
        return area


    def calculate_perimeter(self):
        perimeter = self.width * self.length
        perimeter2 = perimeter * 2
        return perimeter2


if __name__ == '__main__':
    rectangle = Rectangle(5, 3)
    print("Largeur:", rectangle.width)
    print("Longueur:", rectangle.length)
    print("Aire:", rectangle.calculate_area())
    print("Périmètre:", rectangle.calculate_perimeter())
