""" Der ICI Alistirma
The deposit and withdraw methods each change the account balance.
The withdraw method also deducts a fee of 5 dollars from the balance if the withdrawal (before any fees) results in a negative balance. 
Since we also have the method get_fees you will need to have a variable to keep track of the fees paid.
Here's one possible test of the class. 
It should print the values 10 and 5, respectively, since the withdrawal incurs a fee of 5 dollars.
 """

class BankAccount:

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        self.fees = 0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.initial_balance += amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """
        if self.initial_balance - amount < 0:
            self.initial_balance = self.initial_balance - amount - 5
            self.fees +=5
        else:
            self.initial_balance -= amount
                        
    def get_balance(self):
        """Returns the current balance in the account."""
        return f"Your current balance is {self.initial_balance}"
    
    def get_fees(self):
        return f"Your fee is: {self.fees}"

########## Test your code by uncommenting the 4 lines below ########
"""Test output should be that 10 and 5 are printed. """


my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print (my_account.get_balance(), my_account.get_fees())


######### Once your code passes the test, uncomment ########
######### the following 44 lines (all lines below)  ########
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print (my_account.get_balance(), my_account.get_fees())


########## Test your code by uncommenting the 4 lines below ########
""" Test output should be that 10, 5, 5, and 0 are printed.  """
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print (account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees())

########## Once your code passes the test, uncomment ########
########## the following 55 lines (all lines below)  ########​
account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print (account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees())