from peewee import *

db = SqliteDatabase('records.sqlite')

# Model class created to produce columns in database
class Record(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

# connected to database
    class Meta:
        database = db

# set string return statement
    def __str__(self):
        return f'Name: {self.name} | Country: {self.country} | Catches: {self.catches}'

def main():

    while True:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            new_record()
        elif choice == 2:
            search_record()
        elif choice == 3:
            edit_record()
        elif choice == 4:
            delete_record()
        elif choice == 'Q'.upper():
            break

def print_menu():
    print('1: New Record')
    print('2: Search')
    print('3: Edit a record')
    print('4: Delete a record')

def get_menu_choice():
    choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice

def new_record():
    print('works')
    # return
def search_record():
    return
def edit_record():
    return
def delete_record():
    return


if __name__ =='__main__':
    main()
