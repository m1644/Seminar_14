import pytest
from sem_01 import removes_all_except_latin


''' Задание №4
📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

@pytest.mark.parametrize('text,expected', [
    ('Hello World!', 'hello world'),
    ('Hello WORLD!', 'hello world'),
    ('Hello, World!', 'hello world'),
    ('Привет, мир!', ' '),
    ('Hello, World! 123ABC Привет мир!', 'hello world abc  ')
])

def test_removes_all_except_latin(text, expected):
    assert removes_all_except_latin(text) == expected

if __name__ == '__main__':
    pytest.main(['-v'])
