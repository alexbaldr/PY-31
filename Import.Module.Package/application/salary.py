# print("from salary.py")


def calculate_salary(got_salary_per_day ): 

    day = int(input("Запрашиваемое колличество дней: "))
    salary = day * got_salary_per_day 
    return salary

if __name__ == '__main__':
    print(calculate_salary(2) )

