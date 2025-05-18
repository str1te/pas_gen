import random

class PasswordGenerator:
    library = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&*'
    library = list(library)
    def __init__(self, password_length: int): #Присвоим заданную длину пароля
        self.password_length = password_length
    def generate_password(self): #Функция генерации пароля
        if self.password_length <= 0:
            raise ValueError('Password length must be greater than 0')
        count_library = self.library.copy()
        while len(self.library) < self.password_length: #Если длина больше чем библиотека, то просто увеличиваем её
            count_library = count_library*2
        random.shuffle(count_library)

        return ''.join(count_library[:self.password_length])

if __name__ == '__main__':
    length = int(input("Enter length of password: ")) #Задаём длину
    password_generator = PasswordGenerator(length)
    print(password_generator.generate_password())

