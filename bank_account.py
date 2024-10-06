class BankAccount:
    interest_rate = 0.05

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount, target_account=None):
        if target_account is None:
            target_account = self  # Deposit into the current account if no target is specified
        target_account.balance += amount
        print(f"Deposited ${amount} into {target_account.account_holder}'s account. New balance: ${target_account.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds in {self.account_holder}'s account.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.account_holder}'s account. New balance: ${self.balance}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied to {self.account_holder}'s account: ${interest}. New balance: ${self.balance}")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

#  these are the Bank Accounts
account1 = BankAccount("BLESSED ROLLAND")
account2 = BankAccount("JOHN SNOW", 1000)

# this Performs deposits and withdrawals with details
account1.deposit(5000)  # Deposits $5000 into account1
print(f"Transaction details:")
account1.display_account_info()  # Display account1 information

account2.deposit(3000)  # Deposit $3000 into account2
print(f"Transaction details:")
account2.display_account_info()  # Display account2 information

account1.withdraw(2000)  # Withdraw $2000 from account1
print(f"Transaction details:")
account1.display_account_info()  # Display account1 information

account2.withdraw(1500)  # Withdraw $1500 from account2
print(f"Transaction details:")
account2.display_account_info()  # Display account2 information

# this Applys the interest
account1.apply_interest()
print(f"Transaction details:")
account1.display_account_info()  # Display account1 information

account2.apply_interest()
print(f"Transaction details:")
account2.display_account_info()  #this  Displays account2 information

# Depositing  into the accounts
account1.deposit(1000, account2)  # this makes Deposit $1000 from account1 to account2
print(f"Transaction details:")
account2.display_account_info()  # this Displays account2 information