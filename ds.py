import csv
import os.path


header_contacts =['id','User_firstName', 'User_lastName', 'phone_number']
data_bd = 'data_user.csv'
#Создает шапку списка контактов
def create_header(data, header ):
    with open(data, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)

#Добавляет новый контакт
def append_contact(data, contact):
    with open(data, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(contact)

#Создает контакт
def create_contact(data):
    contact_create = input('Введите Имя Фамилия и номер телефона через пробел: ')
    contact = list(map(lambda x: x, contact_create.split()))
    with open(data, 'r' ) as file:
        reader = csv.DictReader(file, delimiter=';')
        count=0
        
        for i in reader:
            
            count+=1
    contact.insert(0, count)        
    return contact

#Просмотр списка контактов
def show_contact(data):
    with open(data, 'r' ) as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for row in reader:
            print(row['id'], '|',row['User_firstName'], '|', row['User_lastName'], '|',row['phone_number'])


    
    

def main():
    if os.path.isfile('data_user.csv'):
        print('База загружается....')
        append_contact(data_bd, create_contact(data_bd))
        show_contact(data_bd)
    else:
        print('Создаем базу....')
        create_header(data_bd, header_contacts)
        
        append_contact(data_bd, create_contact(data_bd))
        show_contact(data_bd)
# main()


def delite_contact(data):
    index = int(input('Введите номер строки для удаления: '))
    with open(data, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        li = list(reader)
        li.pop(index)
        count = 0
        contacts = []
        for i in li:
            
            i['id']=count
            count+=1
        for i in li:
            contacts.append(i.items())
    with open(data, 'r+') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(contacts)
    
show_contact(data_bd)
delite_contact(data_bd)
show_contact(data_bd)