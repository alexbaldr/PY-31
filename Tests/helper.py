documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аркадий Петрович"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


# ДОП ФУНКЦИЯ ПО ИСКЛЮЧЕНИЯМ "name": "Аркадий Петрович"
def get_names():
    for document in documents:
        try:
            print(document['name'])
        except KeyError as e:
            print("Имени нет. Ошибка KeyError ", e)


def get_peaple(documents_dict):
    '''
  p – people – команда, которая спросит номер
  документа и выведет имя человека, которому
  он принадлежит
    '''
    num = input("Номер документа: ")
    for document in documents_dict:
        if document['number'] == num:
            print(document['name'])


def get_full_list(documents_dict):
    '''
  l– list – команда, которая выведет список всех документов
  в формате passport "2207 876234" "Василий Гупкин";
    '''
    for document in documents_dict:
        print(f'{document.get("type")} "{document.get("number")}" "{document.get("name")}" ')


def get_shelf(directories):
    """
    Добавляет полку
    """
    shelf_num = input("Введите номер документа: ")
    for key, value in directories.items():
        for i in value:
            if i == shelf_num:
                print(key)


def get_adding(directories, documents):
    num = input("Введите номер документа ")
    t = input("Введите тип документа ")
    n = input("Введите имя владельца ")
    d = input("Введите номер полки ")
    new_dict = {'type': t, 'number': num, 'name': n}
    documents.append(new_dict)
    for new_dict in directories.keys():
        if new_dict == d:
            directories[new_dict].append(str(num))
            break
        else:
            if new_dict != d:
                directories[d] = [num]
                print(f"Добавлено на полку {d} {directories}  {documents}")


def main():
    while True:
        user_input = input("Введите команду  ").lower()
        if user_input == 'p':
            get_peaple(documents)
        elif user_input == 'l':
            get_full_list(documents)
        elif user_input == 's':
            get_shelf(directories)
        elif user_input == 'a':
            get_adding(directories, documents)
        elif user_input == 'q':
            break


if __name__ == "__main__":
    main()
