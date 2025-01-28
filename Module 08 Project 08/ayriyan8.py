# CSC 6003
# Final Project 
# Bank Management Project

# utilize random library to generate random account numbers
import random

# BankAccount Class

"""
    Summary: Bank Account Management system to create bank accounts, deposit funds
    withdraw funds, check the account balance and perform transfers between accounts


    Parameters
    -----------
    account_number (int)
    balance (float)
    amount(float)
    initial_balance(float)
    account_number_1
    account_number_2
    banking
    
"""
# BankAccount Class
class BankAccount:

    # constructor method, creating our instance variables
    def __init__(self, account_number, balance=0 ):
        self.account_number = account_number
        self.balance = balance

    # deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited: {amount}. Total balance: {self.balance}")
    
    # withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Amount withdrawn: {amount}. Balance: {self.balance}")
            return True
        else:
            print("You don't have enough money!")
            return False
    # use loop in Bank class; for prompting
    
    # checking balance
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
    #displaying account details
    def display_account_details(self):
        return f"Account Number: {self.account_number}\nBalance: ${self.balance}"
    
    # Creating the Bank class
class Bank:

    def __init__(self):
        self.accounts = {}
        
    # Prompts the user to enter an initial balance and creates a new bank account 
    # with a unique account number.
    def create_account(self, initial_balance):
        account_number = random.randint(100000, 999999)
        # insures that the new account number generated is not one already in use
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)

        self.accounts[account_number] = BankAccount(account_number, initial_balance)
        print(f"Congrats! You have an account. \nAccount Number: {account_number}. Balance: {initial_balance}")

    # Takes an account number as input and returns the corresponding 
    # BankAccount object from the list of accounts.
    def get_account(self, account_number):
        return self.accounts.get(account_number)

    # Takes an account number and amount as input and deposits the 
    # specified amount into the account.
    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account_number in self.accounts:
            account.deposit(amount)
        else:
            print("Sorry, that account doesn't exist.")

    

    # Takes an account number and amount as input and withdraws the 
    # specified amount from the account.
    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account_number in self.accounts:
            account.withdraw(amount)
        else:
            print("Sorry, that account doesn't exist.")


    # Takes two account numbers and an amount as 
    # input and transfers the specified amount from one account to another.
    def transfer(self, account_number_1, account_number_2, amount):
        account_1 = self.get_account(account_number_1)
        account_2 = self.get_account(account_number_2)
        if account_1 and account_2:
            if amount <= account_1.balance:
                account_1.withdraw(amount)
                account_2.deposit(amount)
                print("Transfer between accounts complete.")
            else:
                print("Amount could not be transferred. Funds do not suffice.")
        else:
            print("Invalid input. Perhaps you input an incorrect account number?")

# Menu function that displays the available operations to the user:
def menu():
    print("Menu")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. Quit")
    
# function that prompts the user for 
# their choice and executes the corresponding operation.
def execute_choice(banking):
    # prompt user for choice
    choice = input("Enter choice: ")
    if choice == "1":
        initial_balance = float(input("Enter initial balance: $"))
        banking.create_account(initial_balance)
    elif choice == "2":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: $"))
        banking.deposit(account_number, amount)
    elif choice == "3":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: $"))
        banking.withdraw(account_number, amount)
    elif choice == "4":
        account_number = int(input("Enter account number: "))
        account = banking.get_account(account_number)
        if account:
            account.check_balance()
        else:
            print("Account not found.")
    elif choice == "5":
        from_account_number = int(input("Enter your account number: "))
        to_account_number = int(input("Enter recipient's account number: "))
        amount = float(input("Enter transfer amount: $"))
        banking.transfer(from_account_number, to_account_number, amount)
    # returning false quits the program
    elif choice == "6":
        return False
    # Else statement to catch any input that is invalid
    else:
        print("Invalid choice. Please try again.")
    return True

# Recursive function that asks the user if they want to continue 
# performing operations after each operation. 
# If the user chooses to continue, the function should call execute_choice again; 
# otherwise, it should exit the program.
def continue_operation(banking):
    choice = input("\nDo you want to continue (y/n)? ")
    if choice.lower() == "y":
        return execute_choice(banking)
    else:
        return False

# main function that creates a Bank instance and continues to display 
# the menu options and runs the execute_choice 
# function and asks user if they want to continue
def main():
    banking = Bank()
    while True:
        menu()
        if not execute_choice(banking):
            break
        if not continue_operation(banking):
            break

# calling the main function
if __name__ == "__main__":
    main()