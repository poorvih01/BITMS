class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty, amount):
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")

    def deposit(self, amount):
        account=input("enter the amount ")
        print(" ",account.deposit)
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions
'''while(1):
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

choice = input("Enter your choice: ")

if choice == '5':
    print("Exiting program.")
    

if choice in choices:
    if choice == '1' or choice == '2':
        amount = float(input("Enter amount: "))
        choices[choice](account, amount)
            
    else:
        print(choices[choice](account))
else:
    print("Invalid choice. Please try again.")'''

# Example usage:
account = BankAccount(1000)
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)
print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())