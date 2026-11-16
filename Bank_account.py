class BankAccount:
    bank_name = "BOG"
    accounts_count = 0

    def __init__(self, cardtype, owner, balance):
        self.cardtype = cardtype
        self.owner = owner 
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else: 
             raise ValueError("Amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Not enough balance")

    def _update_balance(self, amount):
        self.__balance = amount

    @property
    def balance(self):
        """Getter function"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")

    @balance.deleter
    def balance(self):
        print("Balance record deleted.")
        del self.__balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def calculate_tax(amount):
        return amount * 0.18

class SavingsAccount(BankAccount):

    def __init__(self, card_type, owner, balance, interest_rate):
        super().__init__(card_type, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

    def withdraw(self, amount):
        fee = 4
        total = amount + fee

        if amount > 0 and total <= self.balance:
            self.balance -= total
        else: 
            raise ValueError("not enough balance")

class Creditaccount (BankAccount):
    def __init__(self, card_type, owner, balance, credit_limit):
        super().__init__(card_type, owner, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= -self.credit_limit:
            self._update_balance(self.balance - amount)
            print(f"{amount} GEL withdrawn.")
        else:
            raise ValueError("Credit limit exceeded!")



b1 = BankAccount("Visa", "John", 1000)

s1 = SavingsAccount("Mastercard", "Anna", 2000, 5)

c1 = Creditaccount("Visa", "David", 500, 2000)

b1.deposit(500)
b1.withdraw(200)

print("Bank Account:", b1.balance)

s1.apply_interest()
s1.withdraw(100)

print("Savings Account:", s1.balance)

c1.withdraw(1000)

print("Credit Account:", c1.balance)

BankAccount.change_bank_name("TBC")

print("Bank name:", BankAccount.bank_name)

print("Tax:", BankAccount.calculate_tax(1000))

print("Total accounts:", BankAccount.accounts_count)