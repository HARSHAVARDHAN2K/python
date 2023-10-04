class BankAccount: #BankAccount is NOT a type of Bank
    def __init__(self, accountNumber, name, password, balance):
        self._account_number=accountNumber
        self._name=name
        self._password=password
        self._balance=balance

    def authenticate(self, password):
        if password==self._password:
            return True
        else:
            return False

    def change_password(self, oldPassword, newPassword):
        if self.authenticate(oldPassword):
            self._password=newPassword
       
    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
            return True
        else:
            return False

    def withdraw(self, amount, password):
        if amount<0:
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

    #def info(self):
    def __str__(self):
        return f'BankAccont[AccountNumber={self._account_number},Name={self._name},Balance={self._balance}]'