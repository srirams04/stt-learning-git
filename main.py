"""This module is coded to understand the usage of Pylint in a github workflow"""

class Rectangle:
    """ A rectangle has 2 attributes """
    def __init__(self, length, breadth):
        """ Initialising """
        self.length = length
        self.breadth = breadth

    def area(self):
        """ Calculating area """
        return self.length * self.breadth

    def perimeter(self):
        """ Calculating perimeter """
        return 2 * (self.length + self.breadth)

def main():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    rect = Rectangle(length, breadth)

    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")

if __name__ == "__main__":
    main()
