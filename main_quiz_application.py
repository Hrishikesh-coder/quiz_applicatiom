import sqlite3
from datetime import datetime

db = sqlite3.connect(f'quiz_db.db')

cursor = db.cursor()

def home():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if str(current_time[0:2]) < "12":
        print("Good Morning Teacher!")

    elif str(current_time[0:2]) >= "12" and str(current_time) <= "16":

        print("Good Afternoon !!")

    elif str(current_time[0:2]) > "16" and str(current_time[0:2]) <= "20":

        print("Good Evening !!")

    else:
        print("Good Evening !!")

    print("ARE YOU A STUDENT OR A TEACHER ?")

    answer = input()

    if 'teacher' in answer or 'Teacher' in answer:

        teacher_home()

    else:
        student_home()

def create_table():

    sql = f'''
                CREATE TABLE quiz (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    question          VARCHAR(256) NOT NULL,
                    answer_given               VARCHAR(256) NOT NULL,
                    correct_answer              VARCHAR(256),
                    marks_for_answer     VARCHAR(256)
                );'''

    cursor.execute(sql)
    db.commit()

    sql = f'''
                            CREATE TABLE  user_records (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                name          VARCHAR(256) NOT NULL,

                                obtained_marks  INTEGER NOT NULL,
                                total_marks  INTGER NOT NULL
                            );'''

    cursor.execute(sql)
    db.commit()

    sql = f'''
                        CREATE TABLE questions (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            question          VARCHAR(256) NOT NULL,

                            correct_answer              VARCHAR(256),
                            marks_for_answer     VARCHAR(256)
                        );'''

    cursor.execute(sql)
    db.commit()

    sql = f'''
                    CREATE TABLE questions (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        question          VARCHAR(256) NOT NULL,
                          
                        correct_answer              VARCHAR(256),
                        marks_for_answer     VARCHAR(256)
                    );'''

    cursor.execute(sql)
    db.commit()

    sql = f'''
                    CREATE TABLE  teachers (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name          VARCHAR(256) NOT NULL,
                        
                        password              VARCHAR(256) NOT NULL
                        
                    );'''

    cursor.execute(sql)
    db.commit()

    sql = f'''
                        CREATE TABLE  students (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            name          VARCHAR(256) NOT NULL,

                            password              VARCHAR(256) NOT NULL

                        );'''

    cursor.execute(sql)
    db.commit()

def teacher_or_student():

    print("ARE YOU ARE A STUDENT OR A TEACHER ?")
    entry = input()

    if 'teacher' in entry or 'Teacher' in entry:

        teacher_home()

    else:

        student_home()


def student_home():

    print("WELCOME TO BHANJA'S QUIZ !! DO YOU WANT TO PLAY A QUIZ ?")
    answer = input()

    if 'Y' in answer or 'y' in answer:
        print("THAT'S GREAT")
        print("DO YOU HAVE AN ACCOUNT ?")

        choice = input()

        if 'Yes' in choice or 'yes' in choice:
            answer_questions()

        else:
            create_new_account_for_student()

    else:
        print("OK !! BYE !!")

def teacher_home():


    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if str(current_time[0:2]) < "12":
        print("Good Morning Teacher!")

    elif str(current_time[0:2]) >= "12" and str(current_time) <= "16":

        print("Good Afternoon !!")

    elif str(current_time[0:2]) > "16" and str(current_time[0:2]) <= "20":

        print("Good Evening !!")

    else:
        print("Good Evening !!")

    print("Do you want to set the quiz ?")

    input_given = input()

    if 'y' in input_given or 'Y' in input_given:

        set_questions()

    else:

        print("OK !! THANK YOU FOR VISITING US !! BYE !!")

def create_new_account_for_student():
    print("DO YOU WANT TO CREATE A NEW ACCOUNT ?")

    answer = input()

    if 'Y' in answer or 'y' in answer:

        print("Lets get started !!")

        new_student = []

        name = input("Enter your name")
        password = input("Enter your password")

        new_student.append(name)
        new_student.append(password)

        create_new_account(new_student, 'student')

    else:

        print("OK !! BYE !!")


def set_questions():

    print("DO YOU HAVE AN ACCOUNT ?")

    answer = input()

    if 'Y' in answer or 'y' in answer:

        print("PLEASE LOGIN FIRST !!")

        val = login('teacher')

        if val == True:

            print("OK !! LET'S START CREATING THE QUESTIONS !!")

            print("HERE, YOU HAVE TO GIVE THE QUESTION , CORRECT ANSWER, AND THE MARKS FOR THE CORRECT ANSWER .")
            print("START ENTERING !!")

            entries = []

            question = input("Enter the question !")
            correct_answer = input("Enter the correct answer !")
            marks = int(input("Enter the marks for a correct answer"))

            entries.append(question)
            entries.append(correct_answer)
            entries.append(marks)

            sql = f"INSERT INTO questions(question, correct_answer, marks_for_answer) VALUES('{entries[0]}', '{entries[1]}', '{entries[2]}' )"

            cursor.execute(sql)
            db.commit()

        else:

            print("INCORRECT LOGIN CREDENTIALS GIVEN !!")
    else:
        print("CREATE ONE RIGHT NOW !! WE ARE REDIRECTING YOU TO THE NEW ACCOUNT CREATION OPTION")

        create_new_account_for_teacher()

def answer_questions():
    print("DO YOU HAVE AN ACCOUNT ?")

    answer = input()

    if 'Y' in answer or 'y' in answer:

        print("PLEASE LOGIN FIRST !!")

        val = login('student')

        if val == True:

            name = input("What is Your Name ?")

            print(f"OK , {name} !!  LET'S START ANSWERING THE QUESTIONS !!")

            print("HERE, YOU HAVE TO ANSWER ALL THE QUESTIONS , FULL MARKS WILL BE DISPLAYED AT THE END")

            questions = get_questions()

            obtained_marks = 0
            total_marks = 0

            for question in questions:
                print("START ENTERING !!")

                print(question[1])
                print("The Marks for the correct Answer is : " + str(question[3]))
                entries = []


                answer_given = input("Enter the correct answer !")


                if str(answer_given)  == str(question[2]):

                    obtained_marks+= int(question[3])
                else:

                    obtained_marks+=0

                total_marks += int(question[3])

                sql = f"INSERT INTO quiz(question, answer_given , correct_answer, marks_for_answer) VALUES('{question[1]}', '{answer_given}' , '{question[2]}', '{question[3]}' )"

                cursor.execute(sql)
                db.commit()



            print("Do you want to view your results ?")

            choice = input()

            if 'yes' in choice or 'Yes' in choice:

                print("Your obtained marks : " + str(obtained_marks))
                print("The total marks : " + str(total_marks))

            else:

                print("OK !! BYE !!")

            sql = f"INSERT INTO user_records(name, obtained_marks, total_marks) VALUES('{name}', '{obtained_marks}' , '{total_marks} ')"

            cursor.execute(sql)
            db.commit()

        else:

            print("INCORRECT LOGIN CREDENTIALS GIVEN !!")
    else:
        print("CREATE ONE RIGHT NOW !! WE ARE REDIRECTING YOU TO THE NEW ACCOUNT CREATION OPTION")

        create_new_account_for_teacher()

def get_questions():
    sql = f"SELECT * FROM questions"

    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()

def create_new_account_for_teacher():

    print("DO YOU WANT TO CREATE A NEW ACCOUNT TEACHER ?")

    answer = input()

    if 'Y' in answer or 'y' in answer:



        print("Lets get started !!")

        new_teacher = []

        name = input("Enter your name")
        password = input("Enter your password")

        new_teacher.append(name)
        new_teacher.append(password)

        create_new_account(new_teacher, 'teacher')

    else:

        print("OK !! BYE !!")

def create_new_account(account_details , account_type):

    if account_type == 'teacher':
        sql = f"INSERT INTO teachers(name, password) VALUES('{account_details[0]}', '{account_details[1]}' )"

        cursor.execute(sql)
        db.commit()

    else:
        sql = f"INSERT INTO students (name, password) VALUES('{account_details[0]}', '{account_details[1]}' )"

        cursor.execute(sql)
        db.commit()


def login(user_type):

    credentials = []

    name = input("Enter your username")
    password = input("Enter your password")

    credentials.append(name)
    credentials.append(password)

    details = login_validation(credentials,user_type)

    if len(details) == 0:

        print("No such account exists")

    if len(details) == 0:

       pass
    else:
        if details[0][2] == password:

            return True

        else:

            return False




def login_validation(details, user_type):

    if user_type == 'Teacher' or user_type == 'teacher':
        sql = f"SELECT * FROM teachers WHERE name='{details[0]}'"

        cursor.execute(sql)
        db.commit()
    elif user_type == 'Student' or user_type=='student':

        sql = f"SELECT * FROM students WHERE name='{details[0]}'"

        cursor.execute(sql)
        db.commit()
    else:

        print("Incorrect User type given")
    return cursor.fetchall()


home()

