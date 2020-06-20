from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary


class Buh:
    def __init__(self,name):
        self.name = name

        get_emp = get_employees()     
        for get_name in get_emp.values():
            if name in get_name["name"]:
                salary_per_day = get_name['salary']
                num_salary = calculate_salary(salary_per_day) 
                d = datetime.today().strftime('%d/%m/%Y')
                print("Зaрплата сотрудника равна", num_salary, "руб.", d)
            else:
                print("Wrong name")



if __name__ == '__main__':
    buh1 = Buh(name = input("Введите имя: ")) # Вася Пупкин & Жора Какойто


