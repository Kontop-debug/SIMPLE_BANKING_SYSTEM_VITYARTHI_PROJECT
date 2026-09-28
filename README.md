# SIMPLE_BANKING_SYSTEM_VITYARTHI_PROJECT

Project Description

The **Python Bank Management System** is a simple console-based banking application developed using Python. It allows users to create bank accounts, access existing accounts, deposit and withdraw money, check account balances, view account details, view transaction history, and close accounts.

The program uses **Object-Oriented Programming (OOP)** concepts through the `Account` and `Bank` classes.

Features

* Create a new bank account
* Automatically generate a 10-digit account number
* Make an initial deposit
* Deposit money into an account
* Withdraw money from an account
* Check current account balance
* View account details
* View transaction history
* Close an existing account
* Validate user inputs
* Prevent withdrawals when funds are insufficient
* Store multiple accounts during program execution

Technologies Used

* **Programming Language:** Python
* **Module Used:** `random`
* **Concepts:** Classes, Objects, Methods, Dictionaries, Loops, Conditional Statements, Exception Handling

Program Structure

### `Account` Class

The `Account` class represents an individual bank account.

It contains:

* Account holder's name
* Account balance
* Account number
* Transaction history

Main methods:

* `generate_account_number()`
* `deposit()`
* `withdraw()`
* `check_balance()`
* `display_details()`
* `view_transactions()`

The account number is generated randomly as a 10-digit number.

### `Bank` Class

The `Bank` class manages all the accounts in the system.

Main methods:

* `create_account()`
* `find_account()`
* `close_account()`
* `perform_transaction()`

Accounts are stored using their account numbers as dictionary keys.

Main Menu

When the program starts, it displays:

```text
===== Welcome to Python Bank =====
1. Create New Account
2. Access Existing Account
3. Close an Account
4. Exit
```

The user can select an option to perform the required banking operation.

Transaction Menu

After accessing an account, the following options are available:

```text
Transaction Menu:
1. Deposit
2. Withdraw
3. Check Balance
4. View Account Details
5. View Transaction History
6. Return to Main Menu
```

These operations are handled by the `perform_transaction()` method.

How to Run

1. Install Python 3 on your computer.
2. Save the program as:

```text
bank.py
```

3. Open a terminal or command prompt.
4. Run:

```bash
python bank.py
```

5. Follow the instructions displayed on the screen.

 Example

```text
===== Welcome to Python Bank =====
1. Create New Account
2. Access Existing Account
3. Close an Account
4. Exit

Enter your choice (1-4): 1

Enter account holder's name: Kathiravan
Enter initial deposit amount: $5000

Account for Kathiravan created successfully.
Your Account Number is: 1234567890
```

The user can then access the account using the generated account number and perform transactions.

 Input Validation

The program checks several invalid inputs, including:

* Empty account holder name
* Negative initial deposit
* Invalid numerical input
* Invalid menu choices
* Invalid withdrawal amount
* Withdrawal amount greater than the available balance
* Non-existent account numbers

For example, withdrawals are permitted only when the amount is greater than zero and does not exceed the current balance.

Limitations

* Account information is stored only while the program is running.
* Data is not saved to a database or file.
* There is no password/PIN authentication.
* The randomly generated account number is not checked for duplicates.
* This is an educational project and is not intended for real banking use.
 Learning Objectives

This project demonstrates:

1. Object-Oriented Programming in Python
2. Class and object creation
3. Encapsulation of account operations
4. Use of dictionaries for data storage
5. Exception handling using `try` and `except`
6. Conditional statements and loops
7. Random number generation
8. Basic transaction management

## 👨‍💻 Conclusion

The Python Bank Management System is a beginner-friendly project that demonstrates how Python can be used to build a simple banking application. It provides practical experience with OOP, input validation, data structures, and transaction handling.
