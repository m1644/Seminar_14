


######## Основы тестирования
'''
1. Функциональное тестирование
    ○ Модульное (компонентное)
    ○ Интеграционное
    ○ Системное
    ○ Регрессионное
    ○ Приемочное
    ○ Смоук
2. Тестирование производительности
    ○ Тестирование отказоустойчивости
    ○ Нагрузочное
    ○ Объемное
    ○ Тестирование масштабируемости
3. Обслуживание (регресс и обслуживание)
    ○ Регрессионное
    ○ Тестирование технического обслуживания
'''

#### Основы doctest

from main import is_prime

print(is_prime(42))
print(is_prime(73))
print('------------------------')


#### Разработка через тестирование, TDD

def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time. Working...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
print('------------------------')


#### Проверка исполняемой документации

import doctest
doctest.testfile('prime.md', verbose=True)


#### Запуск тестов из командной строки

'''
python -m doctest .\prime.py
python -m doctest .\prime.py -v

python -m doctest .\prime.md
python -m doctest .\prime.md -v
'''
