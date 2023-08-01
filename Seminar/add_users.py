import json
import os


''' Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
* загрузка данных (функция из задания 4) 
* вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве 
используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа. 
А если пользователь есть, получите его уровень из множества пользователей.
* добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
'''

class BaseError(Exception):
    pass

class LevelError(BaseError):
    pass

class AccessError(BaseError):
    pass


class User:
    def __init__(self, identifier, name, access_level):
        self.identifier = identifier
        self.name = name
        self.access_level = access_level

    def __eq__(self, other):
        return self.name == other.name and self.access_level == other.access_level

class Project:
    def __init__(self, users_file):
        self.users_file = users_file
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                users_data = json.load(file)
                users_list = [User(identifier, user_data['name'], user_data['access_level']) for identifier, user_data in users_data.items()]
                return users_list
        except FileNotFoundError:
            return []

    def login(self, name, access_level):
        user = User(None, name, access_level)
        if user not in self.users:
            raise AccessError("Ошибка доступа: такого пользователя нет в списке.")
        else:
            user = next(u for u in self.users if u == user)
            print(f"Добро пожаловать, {user.name}! Ваш уровень доступа: {user.access_level}.")

    def add_user(self, name, identifier, access_level):
        new_user = User(identifier, name, access_level)
        if any(u.access_level > access_level for u in self.users):
            raise LevelError("Ошибка уровня: недостаточный уровень доступа для добавления пользователя.")
        else:
            if new_user in self.users:
                raise AccessError("Ошибка доступа: пользователь с таким идентификатором уже существует.")
            else:
                self.users.append(new_user)
                with open(self.users_file, 'w', encoding='utf-8') as file:
                    json.dump({user.identifier: {'name': user.name, 'access_level': user.access_level} for user in self.users}, file, indent=4, ensure_ascii=False)
                print(f"Пользователь '{name}' успешно добавлен с уровнем доступа {access_level}.")


users_file = os.path.abspath('users.json')
project = Project(users_file)
