class PhoneBookEntry:
    def __init__(self, last_name, first_name, middle_name, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_number = phone_number

    def to_string(self):
        return f"{self.last_name}, {self.first_name}, {self.middle_name}, {self.phone_number}"


class PhoneBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.entries.remove(entry)

    def export_to_txt(self, file_name):
        with open(file_name, "w") as file:
            for entry in self.entries:
                file.write(entry.to_string() + "\n")

    def import_from_txt(self, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(", ")
                if len(data) == 4:
                    entry = PhoneBookEntry(data[0], data[1], data[2], data[3])
                    self.add_entry(entry)

    def find_entries_by_name(self, name):
        matching_entries = []
        for entry in self.entries:
            if name.lower() in entry.first_name.lower() or name.lower() in entry.last_name.lower():
                matching_entries.append(entry)
        return matching_entries

    def update_entry(self, entry, last_name=None, first_name=None, middle_name=None, phone_number=None):
        if last_name is not None:
            entry.last_name = last_name
        if first_name is not None:
            entry.first_name = first_name
        if middle_name is not None:
            entry.middle_name = middle_name
        if phone_number is not None:
            entry.phone_number = phone_number

    def delete_entry(self, entry):
        self.entries.remove(entry)


# Пример использования
phone_book = PhoneBook()

entry1 = PhoneBookEntry("Иванов", "Иван", "Иванович", "1234567890")
entry2 = PhoneBookEntry("Петров", "Петр", "Петрович", "9876543210")
phone_book.add_entry(entry1)
phone_book.add_entry(entry2)

# Экспорт в файл
phone_book.export_to_txt("phonebook.txt")

# Очистить справочник
phone_book = PhoneBook()

# Импорт из файла
phone_book.import_from_txt("phonebook.txt")

# Вывести данные из справочника
for entry in phone_book.entries:
    print(entry.to_string())

# Изменить данные записи
matching_entries = phone_book.find_entries_by_name("Петров")
if len(matching_entries) > 0:
    entry_to_update = matching_entries[0]
    phone_book.update_entry(entry_to_update, phone_number="1111111111")

# Удалить запись
matching_entries = phone_book.find_entries_by_name("Иванов")
if len(matching_entries) > 0:
    entry_to_delete = matching_entries[0]
    phone_book.delete_entry(entry_to_delete)

# Вывести обновленные данные из справочника
for entry in phone_book.entries:
    print(entry.to_string())