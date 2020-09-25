from peewee import *
db = SqliteDatabase('records.sqlite')

# Model class created to produce columns in database
class Record(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

# Link to database
    class Meta:
        database = db

# set string return statement
    def __str__(self):
        return f'Name: {self.name} | Country: {self.country} | Catches: {self.catches}'

# connect to the DB and create table
db.connect()
db.create_tables([Record])

def main():
    print('Chainsaw Juggling Record Holders as of July 2018')
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
        elif choice.upper() == 'Q':
            break


def print_menu():
    print('1: New Record')
    print('2: Search')
    print('3: Edit a record')
    print('4: Delete a record')


def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice.upper() != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice


def new_record():
    name = input('\nEnter name: ')
    country = input('Country of origin: ')
    caught = input('Number of chainsaws caught: ')
    while caught.isnumeric() is False:
        caught = input('Number of chainsaws caught (Numbers only): ')
    # object is created from user input and saved into the database
    record = Record(name=name, country=country, catches=caught)
    record.save()
    print()


def search_record():
    search_name = input('Enter name to search for: ')
    # SQL query to return any rows that contain user input
    name_found = Record.select().where(Record.name.contains(search_name))
    if name_found.count() == 0:
        print('No match found\n')
    else:
        for name in name_found:
            print(f'{name}\n')


def edit_record():
    edit_name = input('Enter name of record holder to edit: ')
    # SQL query to return any rows that contain the users string
    name_returned = Record.select().where(Record.name.contains(edit_name))
    if name_returned:
        # loop used to ensure that correct record is altered
        # Also allows for mutltiple records from the same person to be modded
        for record in name_returned:
            print(record)
            edit = input('Edit this record? (Y to proceed): ').upper()
            if edit == 'Y':
                edit_caught = input('How many chainsaws were caught?: ')
                record.catches = edit_caught
                record.save()
                print(f'{record.name} has been updated\n')
    else:
        print('No match found in database\n')


def delete_record():
    delete_name = input('Enter name of record holder you would like to delete: ')
    name_to_delete = Record.select().where(Record.name.contains(delete_name))
    if name_to_delete:
        for record in name_to_delete:
            delete = input(f'Delete {record.name}? Enter Y to delete: ').upper()
            if delete == 'Y':
                rows_deleted = Record.delete().where(Record.name == record.name).execute()
                if rows_deleted:
                    print('Rows deleted:\n', rows_deleted)
    else:
        print('No match found\n')


if __name__ =='__main__':
    main()
