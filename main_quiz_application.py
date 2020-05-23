import sqlite3
from datetime import datetime

db = sqlite3.connect(f'quiz_db.db')

cursor = db.cursor()

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
                    CREATE TABLE users (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name          VARCHAR(256) NOT NULL,
                        teacher_or_student     VARCHAR(256) NOT NULL,
                        password              VARCHAR(256) NOT NULL
                        
                    );'''

    cursor.execute(sql)
    db.commit()

def teacher_or_student():

    print("ARE YOU ARE A STUDENT OR A TEACHER ?")
    entry = input()

    if 't' in entry or 'T' in entry:

        teacher_home()

    else:

        student_home()


def student_home():

    print("WELCOME TO BHANJA'S QUIZ !! DO YOU WANT TO PLAY A QUIZ ?")
    answer = input()

    if 'Y' in answer or 'y' in answer:
        print('''THAT'S GREAT
        DO YOU HAVE AN ACCOUNT ?''')

        choice = input()

        if 'Y' in choice or 'y' in choice:
            pass
        else:
            pass

    else:
        pass

def teacher_home():


    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if str(current_time[0:2]) < "12":
        print("Good Morning Teacher!")

    elif str(current_time[0:2]) >= "12" and str(current_time) <= "4":

        print("Good Afternoon !!")

    elif str(current_time[0:2]) > "4" and str(current_time[0:2]) <= "8":

        print("Good Evening !!")

    else:
        print("Good Night !!")

    print("Do you want to set the quiz ?")

    input_given = input()

    if 'y' in input_given or

teacher_home()


