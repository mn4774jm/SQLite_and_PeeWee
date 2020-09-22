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

db.connect()
db.create_tables([Record])


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
    name = input('Enter name: ')
    country = input('Country of origin: ')
    caught = input('Number of fish caught: ')
    while caught.isnumeric() is False:
        caught = input('Number of fish caught (Numbers only): ')
    record = Record(name=name, country=country, catches=caught)
    record.save()

def search_record():
    search_name = input('Enter name to search for: ')
    name_found = Record.select().where(Record.name == search_name)
    if name_found.count() == 0:
        print('No match found')
    else:
        for name in name_found:
            print(name)

def edit_record():
    edit_name = input('Enter name of record holder to edit: ')
    name_returned = Record.select().where(Record.name == edit_name)
    if name_returned:
        edit_caught = input('How many fish were caught?: ')
        for record in name_returned:
            record.catches = edit_caught
            record.save()

def delete_record():
    delete_name = input('Enter name of record holder you would like to delete: ')
    rows_deleted = Record.delete().where(Record.name == delete_name).execute()
    if rows_deleted:
        print('Rows deleted:', rows_deleted)
    else:
        print('No match found')

if __name__ =='__main__':
    main()
