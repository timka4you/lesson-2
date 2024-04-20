class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def transfer(self, recipient_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} from account {self.account_number} to account {recipient_account.account_number}.")
            print(f"New balance for account {self.account_number}: {self.balance}")
            print(f"New balance for account {recipient_account.account_number}: {recipient_account.balance}")
        else:
            print("Insufficient funds or invalid amount for transfer.")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, owner_name, account_number, initial_balance=0):
        new_account = BankAccount(owner_name, account_number, initial_balance)
        self.accounts.append(new_account)
        print(f"Account for {owner_name} created with account number {account_number}.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, sender_account_number, recipient_account_number, amount):
        sender_account = self.find_account(sender_account_number)
        recipient_account = self.find_account(recipient_account_number)
        if sender_account and recipient_account:
            sender_account.transfer(recipient_account, amount)
        else:
            print("One or both accounts not found.")


# Example usage:
bank = Bank()

bank.add_account("Alice", "123456", 1000)
bank.add_account("Bob", "654321", 500)

bank.deposit("123456", 200)
bank.withdraw("654321", 100)
bank.transfer("123456", "654321", 300)