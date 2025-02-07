class Account:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Your account was deposited by {amount}. Current balance: {self.balance}.")
        else:
            print("The deposit must be more than 0.")
        
    def withdraw(self, amount):
        if amount>self.balance:
            print("ERROR: insufficient funds!")
        elif amount > 0:
            self.balance -= amount
            print(f"{amount} was withdrawn from your account. Current balance: {self.balance}")
        else:
            print("Withdrawal amount must be more than 0.")

    def showBalance(self):
        print(f"{self.owner}, your carrent balance is {self.balance}.")

name=input("Enter your name: ")
balance=int(input("Enter the balance on your bank account: "))
userAccount=Account(name, balance)
userAccount.showBalance()

while(True):
    print("Press D to deposit money on your account. Press W to withdraw. Or press Q to quit.")
    operation=input()
    if operation.capitalize() == "D":
        amount = int(input("Enter the amount to deposit: "))
        userAccount.deposit(amount)
    elif operation.capitalize() == "W":
        amount = int(input("Enter the amount to withdraw: "))
        userAccount.withdraw(amount)
    else:
        break
