class BankAccount:
    def __init__(self,name):
        self.owner=name
        self.balance=0.0
    
    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def deposit(self,amount):
        self.balance-=amount
        return self.balance

account=BankAccount("Jack Sparrow")

print(account.getBalance())
account.deposit(1000)
print(account.getBalance())
account.withdraw(500)
print(account.getBalance())



