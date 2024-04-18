class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Example usage:
if __name__ == "__main__":
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    rectangle = Rectangle(width, height)

    print("Area of the rectangle:", rectangle.calculate_area())
    print("Perimeter of the rectangle:", rectangle.calculate_perimeter())