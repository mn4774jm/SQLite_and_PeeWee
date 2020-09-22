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

# connect to the DB and create table
db.connect()
db.create_tables([Record])

#TODO clean up output and comment functions
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
        elif choice == 'Q'.upper():
            break


def print_menu():
    print('1: New Record')
    print('2: Search')
    print('3: Edit a record')
    print('4: Delete a record')


def get_menu_choice():
    choice = input('\nPlease choose an option (1-4) or press "Q" to quit: ')
    while choice.isnumeric() is False and choice != 'Q':
        choice = input('Please choose an option (1-4) or press "Q" to quit: ')
    if choice.isnumeric():
        choice = int(choice)
    return choice


def new_record():
    name = input('\nEnter name: ')
    country = input('Country of origin: ')
    caught = input('Number of fish caught: ')
    while caught.isnumeric() is False:
        caught = input('Number of fish caught (Numbers only): ')
    record = Record(name=name, country=country, catches=caught)
    record.save()



def search_record():
    search_name = input('Enter name to search for: ')
    name_found = Record.select().where(Record.name.contains(search_name))
    if name_found.count() == 0:
        print('No match found\n')
    else:
        for name in name_found:
            print(f'{name}\n')


def edit_record():
    edit_name = input('Enter name of record holder to edit: ')
    name_returned = Record.select().where(Record.name.contains(edit_name))
    if name_returned:
        edit_caught = input('How many fish were caught?: ')
        for record in name_returned:
            record.catches = edit_caught
            record.save()
            print(f'{edit_name} has been updated\n')
    else:
        print('No match found in database\n')


def delete_record():
    delete_name = input('Enter name of record holder you would like to delete: ')
    name_to_delete = Record.select().where(Record.name.contains(delete_name))
    if name_to_delete:
        for record in name_to_delete:
            delete = input(f'Delete {record.name}? Enter Y to delete: ').upper()
            if delete == 'Y':
                rows_deleted = Record.delete().where(Record.name == delete_name).execute()
                if rows_deleted:
                    print('Rows deleted:', rows_deleted)
    else:
        print('No match found\n')


if __name__ =='__main__':
    main()
