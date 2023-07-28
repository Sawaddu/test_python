class BankAccount:
    def __init__(self, accountNumber, accountName, balance=0):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} is successfully made.")
        else: 
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount} is successfully withdrawn.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def getBalance(self): 
        return self.balance

    def accountDetails(self):
        print("Bank account Details")
        print(f"Bank account number: {self.accountNumber}")
        print(f"Bank account name: {self.accountName}")
        print(f"Bank account balance: {self.balance}")

# Creating bank accounts based on user input
accountNumber1 = input("Enter account number for account 1: ")
accountName1 = input("Enter account name for account 1: ")
initialBalance1 = float(input("Enter initial balance for account 1: "))
account1 = BankAccount(accountNumber1, accountName1, initialBalance1)

accountNumber2 = input("Enter account number for account 2: ")
accountName2 = input("Enter account name for account 2: ")
initialBalance2 = float(input("Enter initial balance for account 2: "))
account2 = BankAccount(accountNumber2, accountName2, initialBalance2)

# Performing operations based on user input
while True:
    print("\nSelect operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Get Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(amount)
    elif choice == '3':
        balance1 = account1.getBalance()
        balance2 = account2.getBalance()
        print(f"Account 1 balance: {balance1}")
        print(f"Account 2 balance: {balance2}")
    elif choice == '4':
        account1.accountDetails()
        account2.accountDetails()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
