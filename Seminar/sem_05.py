import unittest
from rectangle import Rectangle


''' Задание №5
📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса.
'''

class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(20, 10)
        self.assertEqual(r.length, 20)
        self.assertEqual(r.width, 10)
        r = Rectangle(10) 
        self.assertEqual(r.length, 10)
        self.assertEqual(r.width, 10)

    def test_get_perimeter(self):
        r = Rectangle(20, 10)
        self.assertEqual(r.get_perimeter(), 60)
        r = Rectangle(10)
        self.assertEqual(r.get_perimeter(), 40)

    def test_get_area(self):
        r = Rectangle(20, 10)
        self.assertEqual(r.get_area(), 200)
        r = Rectangle(10)
        self.assertEqual(r.get_area(), 100)

    def test_add(self):
        r1 = Rectangle(20, 10)
        r2 = Rectangle(10, 5)
        r3 = r1 + r2
        self.assertEqual(r3.length, 30)
        self.assertEqual(r3.width, 15)

    def test_sub(self):
        r1 = Rectangle(20, 10)
        r2 = Rectangle(10, 5)
        r3 = r1 - r2
        self.assertEqual(r3.length, 10) 
        self.assertEqual(r3.width, 5)

    def test_lt(self):
        r1 = Rectangle(10, 5)
        r2 = Rectangle(20, 10)
        self.assertTrue(r1 < r2)

    def test_eq(self):
        r1 = Rectangle(20, 10)
        r2 = Rectangle(20, 10)
        self.assertTrue(r1 == r2)


if __name__ == '__main__':
    unittest.main()
