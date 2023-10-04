from bank_account import BankAccount

class saving_acc(BankAccount):
    def __init__(self, accountNumber, name, password, balance):
        super().__init__(accountNumber, name, password, balance)

    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
            return True
        else:
            return False

    def withdraw(self, amount, password):
        if self._balance - amount <=5000:
            return False
        elif amount>self._balance:
            return False
        elif not self.authenticate(password):
            return False
        else:
            self._balance-=amount
            return True

    def credit_interest(self,interest_rate):
        self._balance+=(self._balance*interest_rate)/1200