"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print("Такого пользователя не существует.")


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        if self.usernames:
            self.usernames.clear()
            print("Все пользователи забанены")
        else:
            print("Пользователей для забанивания не найдено")


if __name__ == "__main__":
    user_manager = UserManager()
    print(user_manager.get_users())
    user_manager.add_user("Benutzer_1")
    user_manager.add_user("Benutzer_2")
    user_manager.add_user("Benutzer_3")
    print(user_manager.get_users())
    print()

    admin_manager = AdminManager()
    print(admin_manager.get_users())
    admin_manager.add_user("User_1")
    admin_manager.add_user("User_2")
    admin_manager.add_user("User_3")
    print(admin_manager.get_users())
    admin_manager.ban_username("User_36")
    admin_manager.ban_username("User_1")
    print(admin_manager.get_users())
    print()

    super_admin_manager = SuperAdminManager()
    print(super_admin_manager.get_users())
    super_admin_manager.add_user("Usuario_1")
    super_admin_manager.add_user("Usuario_2")
    super_admin_manager.add_user("Usuario_3")
    print(super_admin_manager.get_users())
    super_admin_manager.ban_username("Usuario_36")
    super_admin_manager.ban_username("Usuario_1")
    print(super_admin_manager.get_users())
    super_admin_manager.ban_all_users()
    print(super_admin_manager.get_users())
