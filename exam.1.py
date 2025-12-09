class Animal:
    def __init__(self, name, age):
        self.__name = name      # приватный атрибут
        self.__age = age        # приватный атрибут

    #  Геттеры
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    #  Сеттеры
    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Возраст не может быть отрицательным!")

    # Метод, который будут переопределять наследники
    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределён в дочерних классах")


#  Класс Dog
class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


#  Класс Cat
class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


#  Демонстрация работы
dog = Dog("Шарик", 3)
cat = Cat("Мурка", 5)

print("Исходные звуки:")
print(dog.get_name(), "говорит:", dog.make_sound())
print(cat.get_name(), "говорит:", cat.make_sound())

# Изменяем приватные атрибуты через сеттеры
dog.set_name("Рэкс")
dog.set_age(4)

cat.set_name("Пушок")
cat.set_age(2)

print("\nПосле изменения данных:")
print(dog.get_name(), "-", dog.get_age(), "лет,", "звук:", dog.make_sound())
print(cat.get_name(), "-", cat.get_age(), "года,", "звук:", cat.make_sound())
