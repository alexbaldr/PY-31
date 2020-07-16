import psycopg2 as pg

Student = "Student"
with pg.connect(database='NewDBforMe', user='NewDBforMe',
    password='1SomePassword2', host='pg.codecontrol.ru', port=59432) as con:
    cur = con.cursor()


def create_db():  # создает таблицы

    cur.execute('''create table if not exists Student(
        id serial primary key not null,
        name character varying(100) not null,
        gpa numeric(10,2),
        birth varchar(11)
        );''')

    cur.execute('''create table if not exists Course(
        id integer primary key not null,
        name character varying(100) not null
        );''')

    cur.execute('''create table if not exists Comunicate(
        st_id integer references student(id),
        cur_id integer references course(id)
        );''')
    con.commit()


def del_str(da):
    cur.execute('''delete from Comunicate where st_id=%s;''', (da))
    con.commit()


def del_db():
    # удаляет таблицы
    cur.execute('''drop table Student CASCADE;''')
    con.commit()


def get_students(course_id):  # возвращает студентов определенного курса
    cur.execute('''select Student.name
    from Comunicate
    JOIN Student on Student.id = Comunicate.st_id
    join Course on Course.id = Comunicate.cur_id
    where Course.id = %s
        ;''', (str(course_id)))
    for i in cur.fetchall():
        print(i)


def add_course(course_id, course_name):  # создает курс
    cur.execute('''
        insert into Course(id, name) values( %s, %s);
        ''', (course_id, course_name,))
    con.commit()


def add_links(course_id, student_id,):  # записывает студентов на курс
    cur.execute('''
        insert into Comunicate(st_id, cur_id) values(%s, %s);
        ''', (course_id, student_id,))
    con.commit()


def add_student(student, gpa, birth):  # просто создает студента
    cur.execute('''
        insert into Student(name, gpa, birth) values(%s, %s, %s);
        ''', (student, gpa, birth,))
    con.commit()


def get_all_students_with_course():  # Получаем всех студентов с их курсами
    cur.execute('''select Student.id, Student.name, course.name
        from Comunicate
        JOIN Student on Student.id = Comunicate.st_id
        join Course on Course.id = Comunicate.cur_id
        ;''')
    for i in cur.fetchall():
        print(i)


def get_student(student_id):  # получаем стедента по его id
    cur.execute('''
            select name from Student where id = %s;
            ''', (str(student_id)))
    for i in cur.fetchone():
        print(i)


def get_all_tables():   # Получаем все таблицы.
    cur.execute('''
            select * from Course;
            ''')
    print(cur.fetchall())
    cur.execute('''
            select * from Student;
            ''')
    for i in cur.fetchall():
        print(i)

    cur.execute('''
            select * from Comunicate;
            ''')
    print(cur.fetchall())


# create_db()
# del_db()
# del_str('1')
# add_student('Artemiy','3.8','1988-12-05')
# add_course(4, 'Как создать тайное правительство')
# add_links(3, 4) # student_id, course_id
# get_students(3)
# get_student(3)
# get_all_students_with_course()
# get_all_tables()
