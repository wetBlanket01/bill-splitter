from random import choice


class BillSplitter:
    def __init__(self):
        self.persons = dict()
        self.person_count = int(input('Enter the number of friends joining (including you):\n'))
        if self.person_count > 0:
            self.add_persons()
            self.split_bill()
        else:
            print('\nNo one is joining for the party')

    def add_persons(self):
        print('\nEnter the name of every friend (including you), each on a new line:')
        self.persons = {input(): 0 for _ in range(self.person_count)}

    def split_bill(self):
        bill_value = int(input('\nEnter the total bill value:\n'))
        lucky_person = self.the_lucky_one()

        for person in self.persons:
            if person == lucky_person:
                self.persons[lucky_person] = 0
                continue
            self.persons[person] = round(bill_value / (self.person_count - bool(lucky_person)), 2)

        print(self.persons)

    def the_lucky_one(self):
        option = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if option == 'Yes':
            lucky_person = choice([*self.persons.keys()])
            print(f'\n{lucky_person} is the lucky one!\n')
            return lucky_person
        else:
            print('\nNo one is going to be lucky\n')
            return False


splitter = BillSplitter()
