import unittest


''' Задание_1
📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
📌 Напишите к ним тесты.
📌 2-5 тестов на задачу в трёх вариантах:
    ○ doctest,
    ○ unittest,
    ○ pytest. 
'''

# Задача с факториалом (тест unittest)

class FactorialGenerator:
    def __init__(self, start=1, stop=None, step=1):
        self.start = start
        self.stop = stop if stop is not None else start
        self.step = step

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def generate_factorials(self):
        current = self.start
        while current <= self.stop:
            yield self.factorial(current)
            current += self.step


class TestFactorialGenerator(unittest.TestCase):
    def test_generate_factorials_01(self):
        generator = FactorialGenerator(1, 5)
        self.assertEqual(list(generator.generate_factorials()), [1, 2, 6, 24, 120])

    def test_generate_factorials_02(self):
        generator = FactorialGenerator(2, 10, 2)
        self.assertEqual(list(generator.generate_factorials()), [2, 24, 720, 40320, 3628800])

    def test_generate_factorials_03(self):
        generator = FactorialGenerator(5)
        self.assertEqual(list(generator.generate_factorials()), [120])


if __name__ == "__main__":
    unittest.main(verbosity=2)
