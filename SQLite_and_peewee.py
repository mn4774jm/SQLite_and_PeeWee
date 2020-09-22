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
        get_menu_choice()
        action = get_action()
        action()
        if choice == 'Q'.upper():
            break

def print_menu():


def get_menu_choice():


def get_action():


def new_record():

def search_record():

def edit_record():

def delete_record():




