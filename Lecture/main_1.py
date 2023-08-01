import unittest


#### Метод setUp

class TestSample(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp') # Только для демонстрации работы метода

    def test_append(self):
        self.data.append(11)
        self.assertEqual(self.data, [2, 3, 5, 7, 11])

    def test_remove(self):
        self.data.remove(5)
        self.assertEqual(self.data, [2, 3, 7])

    def test_pop(self):
        self.data.pop()
        self.assertEqual(self.data, [2, 3, 5])


if __name__ == '__main__':
    unittest.main(verbosity=2)


#### Метод tearDown

class TestSample(unittest.TestCase):

    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        from pathlib import Path
        Path('top_secret.txt').unlink()


if __name__ == '__main__':
    unittest.main(verbosity=2)
