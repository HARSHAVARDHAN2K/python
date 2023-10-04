from bank_account import BankAccount

class overDraft_acc(BankAccount):
    def __init__(self, accountNumber, name, password, balance):
        super().__init__(accountNumber, name, password, balance)

    def deposit(self, amount):
        self._eStatement = []
        if amount>0:
            self._balance+=amount
            self._eStatement.append(self._balance)
            return True
        else:
            return False

    def withdraw(self, amount, password):
        if amount <0:
            return False
        elif amount>self._balance:
            return False
        elif not self.authenticate(password):
            return False
        else:
            maximum_bal = max(self._eStatement)
            limit = self._balance+maximum_bal*0.1
            if  limit-amount>=0:
                    print("Limit:",limit)
                    print("state",self._eStatement)
                    odFee = 0
                    if self._balance-amount<0:
                        odFee = (self._balance-amount)*0.01
                        print(f'odFee:{odFee}')
                    self._balance = self._balance - amount + odFee
            return True

    def credit_interest(self,interest_rate):
        self._balance+=(self._balance*interest_rate)/1200


         
            