class Contact:
    def __init__(self, name, phone_number, contact_id=None):
        self.name = name
        self.phone_number = phone_number
        self.id = contact_id

    @staticmethod
    def validate_phone_number(phone_number):
        """Проверяет, что номер состоит ровно из 10 цифр."""
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        """Добавляет новый контакт, предварительно проверяя номер."""

        # 1. Проверка правильности телефона
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")

        # 2. Увеличиваем last_id
        cls.last_id += 1

        # 3. Создаём новый контакт
        new_contact = Contact(name, phone_number, cls.last_id)

        # 4. Добавляем в список
        cls.all_contacts.append(new_contact)

    @classmethod
    def remove_contact(cls, contact_id):
        """Удаляет контакт по id."""
        for contact in cls.all_contacts:
            if contact.id == contact_id:
                cls.all_contacts.remove(contact)
                return
        print(f"Контакт с id={contact_id} не найден.")
print(ContactList.all_contacts)  # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for c in ContactList.all_contacts:
    print(c.id, c.name, c.phone_number)


ContactList.remove_contact(1)

for c in ContactList.all_contacts:
    print(c.id, c.name, c.phone_number)
