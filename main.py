import math
import time
import numpy

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
	self.breadth = breadth



    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

def main():
    length =float(input("Enter the length of the rectangle: "))
    breadth= float(input("Enter the breadth of the rectangle: "))
    rect = Rectangle(length,breadth)

    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")


if __name__ == "__main__":
    main()
