import unittest
from sem_01 import removes_all_except_latin


''' Задание №3
📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

class TestRemovesAllExceptLatin(unittest.TestCase):

    def test_no_change(self):
        text = 'Hello World!'
        expected = 'hello world'
        self.assertEqual(removes_all_except_latin(text), expected)

    def test_case_change(self):
        text = 'Hello WORLD!'
        expected = 'hello world'
        self.assertEqual(removes_all_except_latin(text), expected)

    def test_punctuation(self):
        text = 'Hello, World!'
        expected = 'hello world'
        self.assertEqual(removes_all_except_latin(text), expected)

    def test_non_latin(self):
        text = 'Привет, мир!'
        expected = ' '
        self.assertEqual(removes_all_except_latin(text), expected)

    def test_all(self):
        text = 'Hello, World! 123ABC Привет мир!'
        expected = 'hello world abc  '
        self.assertEqual(removes_all_except_latin(text), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
