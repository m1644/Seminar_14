import pytest
import json
from add_users import User, Project, LevelError, AccessError


''' Задание №6
📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
📌 Напишите 3-7 тестов pytest для данного проекта.
📌 Используйте фикстуры.
'''

@pytest.fixture
def temp_users_file(tmp_path):
    users_data = {
        "1": {"name": "User1", "access_level": 1},
        "2": {"name": "User2", "access_level": 5},
        "3": {"name": "User3", "access_level": 7}
    }
    users_file = tmp_path / "temp_users.json"
    with open(users_file, "w", encoding="utf-8") as file:
        json.dump(users_data, file, indent=4, ensure_ascii=False)
    return users_file

def test_load_users(temp_users_file):
    project = Project(temp_users_file)
    assert len(project.users) == 3
    assert project.users[0].name == "User1"
    assert project.users[1].access_level == 5

def test_login(temp_users_file, capsys):
    project = Project(temp_users_file)
    project.login("User1", 1)
    captured = capsys.readouterr()
    assert "Добро пожаловать, User1! Ваш уровень доступа: 1." in captured.out

    with pytest.raises(AccessError, match="Ошибка доступа: такого пользователя нет в списке."):
        project.login("User4", 4)

def test_add_user(temp_users_file, capsys):
    project = Project(temp_users_file)
    project.add_user("NewUser", "10", 7)
    assert len(project.users) == 4
    assert project.users[3].name == "NewUser"
    assert project.users[3].access_level == 7
    with pytest.raises(LevelError, match="Ошибка уровня: недостаточный уровень доступа для добавления пользователя."):
        project.add_user("AnotherUser", "5", 1)
    with pytest.raises(AccessError, match="Ошибка доступа: пользователь с таким идентификатором уже существует."):
        project.add_user("User3", "3", 7)


if __name__ == '__main__':
    pytest.main(['-v'])
