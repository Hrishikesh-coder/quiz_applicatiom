import sqlite3

db = sqlite3.connect(f'quiz_db.db')

cursor = db.cursor()

def home():

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
