"""HW_10"""


from collections import UserDict


class Field:
    """Field class"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Name class"""
    def __init__(self, value):
        super().__init__(value)
        if not value:
            raise ValueError("Give me a name")


class Phone(Field):
    """Phone class"""
    def __init__(self, value):
        super().__init__(value)
        if value and not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits.")


class Record:
    """Record class"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Add phone"""
        if phone and phone not in self.phones:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Remove phone"""
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """Edit phone"""
        if old_phone in self.phones:
            for index, phone in enumerate(self.phones):
                if phone.value == old_phone:
                    self.phones[index] = Phone(new_phone)
        raise ValueError

    def find_phone(self, phone):
        """Find phone"""
        for i in self.phones:
            if i.value == phone:
                return i
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Address Book"""
    def add_record(self, record):
        """New record in Address Book"""
        self.data[record.name.value] = record

    def find(self, name):
        """Find record data in Address Book"""
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name):
        """Delete record from Address Book"""
        if name in self.data:
            del self.data[name]
