'''
Account checker
'''
class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'Added {amount} to the balance')
        print(f'Account owner: {self.owner}')
        print(f'New balance: {self.balance}')

    def withdraw(self,amount):
        if self.balance < amount:
            print('Funds Unavailable!')
            print(f'Remaining balance: {self.balance}')
        else:
            self.balance = self.balance - amount
            print('Withdrawal Accepted')
            print(f'Remaining balance: {self.balance}')
