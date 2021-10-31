class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password  # тут сразу отрабатывает наш сеттер

    @staticmethod
    def is_include_number(password):
        for digit in '0123456789':
            if digit in password:
                return True
        return False

    @property
    def password(self):
        print('getter called')
        return self.__password

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Пароль слишком короткий')
        if len(value) > 12:
            raise ValueError('Пароль слишком длинный')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        self.__password = value


user1 = User('ivan', '833d')
