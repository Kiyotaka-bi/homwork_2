from datetime import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name

        # приватные атрибуты
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    # ——————————————————
    #      GETTERS
    # ——————————————————

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        """Вычисление возраста исходя из birth_date (доп. задание)."""
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        years = today.year - birth.year

        # если ДР в этом году ещё не наступил – уменьшаем возраст
        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1
        return years

    # ——————————————————
    #      METHODS
    # ——————————————————
    def introduce(self):
        edu_text = (
            "У меня есть высшее образование."
            if self.higher_education
            else "У меня нет высшего образования."
        )

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. {edu_text}"
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_text = (
            "У меня есть высшее образование."
            if self.higher_education
            else "У меня нет высшего образования."
        )

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Я учился с Айсулуу в группе {self.group}. "
            f"{edu_text}"
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = (
            "У меня есть высшее образование."
            if self.higher_education
            else "У меня нет высшего образования."
        )

        print(
            f"Привет, меня зовут {self.name}. "
            f"Моя профессия {self.occupation}. "
            f"Мое хобби {self.hobby}. "
            f"{edu_text}"
        )


# ——————————————————
# TEST
# ——————————————————
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()

print("Возраст Айбека:", fr1.age)
