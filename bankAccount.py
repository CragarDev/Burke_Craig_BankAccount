

# * Craig Burke - Bank Account

""" 
? Assignment: BankAccount

Objectives

Practice writing classes
As we continue thinking about our banking application,
we realize that it would be more accurate to assign a balance not to the user directly,
but that in the real world, users have accounts, and accounts have balances.
This gives us the idea that maybe an account is its own class!
But as we stated, it is not completely independent of a class;
accounts only exist because users open them.

For this assignment, don't worry about putting any user information in the BankAccount class.
We'll take care of that in the next lesson!

Let's first just get some more practice writing classes by writing a new BankAccount class.

The BankAccount class should have a balance.
    When a new BankAccount instance is created, if an amount is given,
    the balance of the account should initially be set to that amount;
    otherwise, the balance should start at $0. 

The account should also have an interest rate, saved as a decimal
    (i.e. 1% would be saved as 0.01), which should be provided upon instantiation.
    (Hint: when using default values in parameters, the order of parameters matters!)

The class should also have the following methods:

deposit(self, amount) - increases the account balance by the given amount
 withdraw(self, amount) - decreases the account balance by the given amount
    if there are sufficient funds; if there is not enough money, print a message
    "Insufficient funds: Charging a $5 fee" and deduct $5
display_account_info(self) - print to the console: eg. "Balance: $100"
yield_interest(self) - increases the account balance by
    the current balance * the interest rate (as long as the balance is positive)

This means we need a class that looks something like this:
"""

""" 
// 1.Create a BankAccount class with the attributes interest rate and balance

// 2. Add a deposit method to the BankAccount class

// 3. Add a withdraw method to the BankAccount class

// 4. Add a display_account_info method to the BankAccount class

// 5. Add a yield_interest method to the BankAccount class

// 6. Create 2 accounts

// 7. To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

// 8. To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

// 9. NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

"""

# Creating the Class


class BankAccount:
    all_bank_accounts = []
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate=5.5, balance=0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.interest_rate = int_rate * .01
        self.account_balance = balance
        BankAccount.all_bank_accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Your deposit of ${amount:,.2f} has been accepted!")
        print("")
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
            print(f"Your withdrawal of ${amount:,.2f} has been completed!")
            print("")
            return self
        else:
            print("Insufficient funds: Charging a $5.00 fee!")
            print("")
            self.account_balance -= 5
            return self

    def display_account_info(self):
        print(f"Your balance is: ${self.account_balance:,.2f}")
        print("")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            intIncrease = self.account_balance * self.interest_rate
            self.account_balance += intIncrease
            print(
                f"You have received ${intIncrease:,.2f} interest on your account!")
            print("")
            return self
        else:
            print("You do not have enough funds to earn interest.")
            print("")
        return self

    @classmethod
    def print_all_balances(cls):
        total_sum = 0
        for each_account in cls.all_bank_accounts:
            total_sum += each_account.account_balance
        # print(f"The balance of all the accounts is:{round(total_sum, 2)}")
        print(f"The balance of all the accounts is: ${total_sum:,.2f}")
        print("")

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount < 0):
            return False
        else:
            return True


# Creating the users accounts
maggieMay = BankAccount()
alreadyRich = BankAccount(12.6, 24000)

# User 1 deposits and withdrawals
maggieMay.deposit(20).deposit(30).deposit(
    50).withdraw(105).yield_interest().display_account_info()
print("")

# User 2 deposits and withdrawals
alreadyRich.deposit(2600).deposit(1965).withdraw(
    1200).withdraw(3689).withdraw(250).withdraw(678).yield_interest().display_account_info()

# printing the total balance of all accounts
BankAccount.print_all_balances()
