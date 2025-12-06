class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я работаю {self.job}.")


class Classmate(Person):
    def __init__(self, name, age, job, group_name):
        super().__init__(name, age, job)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет, я {self.name}, мне {self.age} лет, я одногруппник и учусь в группе {self.group_name}. "
            f"По профессии я {self.job}."
        )


class Friend(Person):
    def __init__(self, name, age, job, hobby):
        super().__init__(name, age, job)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, я {self.name}, мне {self.age} лет, я друг, мое хобби — {self.hobby}. "
            f"Работаю {self.job}."
        )


# --- Создаем объекты ---
classmate1 = Classmate("Бектур", 20, "программист", "Python-14")
classmate2 = Classmate("Айгерим", 19, "дизайнер", "Python-14")

friend1 = Friend("Алмаз", 22, "инженер", "футбол")
friend2 = Friend("Руслан", 23, "тестер", "шахматы")

# --- Вызываем introduce() ---
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

# --------------------------------------------------------------------
# Доп. задание 1
people = [classmate1, classmate2, friend1, friend2]

for person in people:
    person.introduce()

# --------------------------------------------------------------------
# Доп. задание 2
class BestFriend(Friend):
    def __init__(self, name, age, job, hobby, shared_memory):
        super().__init__(name, age, job, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        # вызываем метод Friend
        super().introduce()
        # добавляем уникальную часть
        print(f"Наше любимое общее воспоминание: {self.shared_memory}")


best = BestFriend("Марат", 24, "разработчик", "велоспорт", "поездка на Иссык-Куль")
best.introduce()
