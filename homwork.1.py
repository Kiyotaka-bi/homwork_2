class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_text = "есть высшее образование" if self.higher_education else "высшего образования нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии я {self.occupation}, {edu_text}.")


# Создание экземпляров класса
person1 = Person("Аскат", "12.08.2005", "программист", True)
person2 = Person("Данияр", "23.04.2004", "дизайнер", False)
person3 = Person("Айгуль", "14.01.1998", "бухгалтер", True)

# Печать атрибутов
print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

print("\n--- Представление ---")
person1.introduce()
person2.introduce()
person3.introduce()
