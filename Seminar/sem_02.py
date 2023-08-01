import doctest
import string


''' Задание №2
📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

def removes_all_except_latin(text):
    """
    Removes all characters from the text except latin letters and spaces.
    
    >>> removes_all_except_latin('Hello World!')
    'hello world'
    
    >>> removes_all_except_latin('Hello WORLD!')
    'hello world'
    
    >>> removes_all_except_latin('Hello, World!')
    'hello world'
    
    >>> removes_all_except_latin('Привет, мир!')
    ' '
    
    >>> removes_all_except_latin('Hello, World! 123ABC Привет мир!')
    'hello world abc  '
    """
    text = text.lower()
    letters = string.ascii_lowercase + ' '
    cleaned_text = ''.join(char for char in text if char in letters)
    return cleaned_text


if __name__ == '__main__':
    # doctest.testmod()
    doctest.testmod(verbose=True)
