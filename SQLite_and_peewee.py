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


