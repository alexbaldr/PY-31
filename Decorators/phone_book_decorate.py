import json
from logger import get_path

@get_path ("log.txt")
class Contact:
    def __init__(self, name, lastname, number, favourites = False, **kwargs):
        self.name = name
        self.number = number
        self.lastname = lastname
        self.favourites = favourites
        self.kwargs = [(f'{key}: {value}') for key, value in kwargs.items()]

    def __str__(self):
        if self.favourites == False:
            favourites = "нет"
        else:
            favourites = "да"
        other_info = '\n\t\t'.join(self.kwargs)
        return f'''
            Имя:{self.name} 
            Фамилия: {self.lastname} 
            Телефон: {self.number} 
            В избранных: {favourites} 
            Дополнительная информация: 
                {other_info}'''


class Phone_book:
    contacts_list = []

    def __init__(self, name):
        self.name = name

    def add_contact(self, Contact):
        self.contacts_list.append(Contact)
        return Contact
 
    def find_contact(self, name, lastname):
        for contact in self.contacts_list:
            if contact.name == name and contact.lastname == lastname:
                print(contact)

    def del_contact(self, name, lastname):
        for contact in self.contacts_list:
            if contact.name == name and contact.lastname == lastname:
                self.contacts_list.remove(contact)

    def get_favourites(self):
        for contact in self.contacts_list:
            if contact.favourites == True:
                print(contact)


    def get_full_list(self):
        for i in self.contacts_list:
            print (i)
            


phone_book = Phone_book("Телефонная книга")
phone_book.add_contact(Contact('Mike', 'Smith', '+71234567810', favourites =True, telegram='@mike', email='miky@smith.com'))
phone_book.add_contact(Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com'))
phone_book.add_contact(Contact('Jorg', 'Mihaile', '+7177511156',  email='jm@mail.ru'))
# phone_book.get_favourites()
# phone_book.del_contact('Jhon', 'Smith')
phone_book.get_full_list()