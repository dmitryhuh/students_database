import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        self.connect()
        if not self.connection:
            raise Exception("Database connection is not established.")
        
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        data = cursor.fetchall()
        self.close()
        return data
    
db = DatabaseManager("students.db")

while True:
    print("0. Вихід")
    print("1. Показати всіх студентів")
    print("2. Показати всі курси")
    print("3. Додати студента")
    print("4. Додати курс")
    print("5. Записати студента на курс")
    print("6. Показати курси студента")
    print("7. Показати студентів курсу")

    choice = input('Оберіть дію:')
    if choice == "0":
        break
    elif choice == "1":
        students = db.execute_query("SELECT * FROM students")
        for student in students:
            print(student)
    elif choice == "2":
        courses = db.execute_query("SELECT * FROM courses")
        for course in courses:
            print(courses)
    elif choice == "3":
        name = input()
        age = input()
        major = input()
        db.execute_query("INSERT INTO students (name, age, major) VALUE (?, ?, ?)", (name, age, major))