import string


''' Задание №1
📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.
'''

def removes_all_except_latin(text):
    text = text.lower()
    letters = string.ascii_lowercase + ' '
    cleaned_text = ''.join(char for char in text if char in letters)
    return cleaned_text


input_text = 'Hello World! Привет мир! 123abc'
print(removes_all_except_latin(input_text))
