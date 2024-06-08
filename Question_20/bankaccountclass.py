class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number 
        self.account_holder = account_number 
        self.balance = balance 
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount 
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount 
    def get_balance(self):
        return self.balance 

bank_account = BankAccount("12345678","John Doe",300.0)
bank_account.deposit(200.0)
bank_account.withdraw(100.0)
print(bank_account.get_balance())