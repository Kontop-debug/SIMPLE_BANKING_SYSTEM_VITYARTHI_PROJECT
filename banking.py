import random

class Account:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.account_number = self.generate_account_number()
        self.transactions = []
        print(f"Account for {self.name} created successfully.")
        print(f"Your Account Number is: {self.account_number}")

    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance for account {self.account_number}: ${self.balance:.2f}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
        print("-----------------------")

    def view_transactions(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter account holder's name: ")
        if not name.strip():
            print("Name cannot be empty.")
            return
        
        try:
            initial_deposit = float(input("Enter initial deposit amount: $"))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative.")
                return
            new_account = Account(name, initial_deposit)
            self.accounts[new_account.account_number] = new_account
        except ValueError:
            print("Invalid input for deposit. Please enter a valid number.")

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def close_account(self):
        account_number = input("Enter the account number to close: ")
        account = self.find_account(account_number)
        if account:
            confirm = input(f"Are you sure you want to close the account for {account.name}? (yes/no): ").lower()
            if confirm == 'yes':
                del self.accounts[account_number]
                print("Account closed successfully.")
            else:
                print("Account closure cancelled.")
        else:
            print("Account not found.")

    def perform_transaction(self):
        account_number = input("Enter your account number: ")
        account = self.find_account(account_number)

        if not account:
            print("Account not found. Please check the account number and try again.")
            return

        print(f"\nWelcome, {account.name}!")
        while True:
            print("\nTransaction Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. View Account Details")
            print("5. View Transaction History")
            print("6. Return to Main Menu")
            
            try:
                choice = int(input("Enter your choice (1-6): "))
                if choice == 1:
                    amount = float(input("Enter amount to deposit: $"))
                    account.deposit(amount)
                elif choice == 2:
                    amount = float(input("Enter amount to withdraw: $"))
                    account.withdraw(amount)
                elif choice == 3:
                    account.check_balance()
                elif choice == 4:
                    account.display_details()
                elif choice == 5:
                    account.view_transactions()
                elif choice == 6:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    my_bank = Bank()
    while True:
        print("\n===== Welcome to Python Bank =====")
        print("1. Create New Account")
        print("2. Access Existing Account")
        print("3. Close an Account")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                my_bank.create_account()
            elif choice == 2:
                my_bank.perform_transaction()
            elif choice == 3:
                my_bank.close_account()
            elif choice == 4:
                print("Thank you for using Python Bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()   
