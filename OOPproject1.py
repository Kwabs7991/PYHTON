#Object Oriented Project 001: Creating a Bank Account.
#Name: Kobbie Mike Tabi
#Date: 22/07/2020

class BankAcc:

    def __init__(self):
        self.balance = 0

    #this function will take in the amount of money you put in as deposit
    def deposit (self, deposit_amount):
        self.balance = self.balance + deposit_amount

    #This will take the amount you want to withdraw as an arg.
    def withdrawal(self, with_amount):
        if self.balance >= with_amount:
            self.balance -= with_amount #This is the same as writing "self.balance = self.balance - with_amount"
        else:
            print("You have Insufficient funds available.")

    def display_balance(self):
        return f"Current Balance remaining: \xA3{self.balance}"

account1 = BankAcc() # creating an instance of the object,thus creating your bank account.
account2 = BankAcc() # creating an instance of the object,thus creating another bank account.
account3 = BankAcc() # creating an instance of the object,thus creating a third bank account.
account1.deposit(180) # This is the owner of account1 depositing £180.
account1.deposit(100)
account2.deposit(1000)
account2.deposit(1000)
account2.deposit(1)

print(account1.display_balance())
print(account2.display_balance())
print(account3.display_balance())

print("\n\n\n")

account2.withdrawal(501)
account1.withdrawal(700)
print(account1.display_balance())
print(account2.display_balance())
