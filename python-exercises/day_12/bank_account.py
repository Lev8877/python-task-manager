class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance 

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно денег на балансе")
        
    def show_balance(self):
        print(f"Денег на счету: {self.balance}")


user = BankAccount("Лев", 5800000000000000000000000000000000000000000000000000000000000000000000000000000)

user.deposit(1)
print(user.balance)
user.withdraw(1)
print(user.balance)
user.show_balance()