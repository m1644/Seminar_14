

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None or width == "" else width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сложить только два прямоугольника")
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Можно вычесть только другой прямоугольник")
        new_length = self.length - other.length
        new_width = self.width - other.width
        new_length = max(new_length, 0)
        new_width = max(new_width, 0)
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() < other.get_area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() >= other.get_area()
