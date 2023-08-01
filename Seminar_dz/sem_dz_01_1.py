import doctest


''' Задание_1
📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
📌 Напишите к ним тесты.
📌 2-5 тестов на задачу в трёх вариантах:
    ○ doctest,
    ○ unittest,
    ○ pytest. 
'''

# Задача с факториалом (тест doctest)

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

    def __str__(self):
        return f"FactorialGenerator(start={self.start}, stop={self.stop}, step={self.step})"


def test_factorial_generator():
    """
    >>> generator = FactorialGenerator(1, 5)
    >>> list(generator.generate_factorials())
    [1, 2, 6, 24, 120]

    >>> generator = FactorialGenerator(2, 10, 2)
    >>> list(generator.generate_factorials())
    [2, 24, 720, 40320, 3628800]

    >>> generator = FactorialGenerator(5)
    >>> list(generator.generate_factorials())
    [120]
    """
    pass  # doctest will automatically run the tests embedded in the docstring


if __name__ == "__main__":
    doctest.testmod(verbose=True)
