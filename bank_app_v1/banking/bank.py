from accounts.saving_acc import saving_acc
from accounts.overdraft_acc import overDraft_acc
from accounts.current_acc import current_acc

class Bank:
    def __init__(self, name,interest_rate):
        self. _name=name
        self.interest_rate=interest_rate
        self._last_id=0
        self._accounts=[]

    def open_account(self, acc_type, name, password, balance):
        self._last_id+=1
        if acc_type == "SA":
            account = saving_acc(self._last_id, name, password, balance)
        elif acc_type == "ODA":
            account = overDraft_acc(self._last_id, name, password, balance)
            print()
        else:
            account = current_acc(self._last_id, name, password, balance)
            print()
        self._accounts.append(account)
        return account._account_number

    def close_account(self, account_number, password):
        account=self.get_account(account_number)
        if account is None:
            return None
        elif not account.authenticate(password):
            return None
        elif account._balance<0:
            return None
        else:
            self._accounts.remove(account)
            return account._balance
    
    def get_account(self, account_number):
        for account in self._accounts:
            if account._account_number==account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account=self.get_account(account_number)
        if account:
            return account.deposit(amount)
        else:
            return False


    def withdraw(self, account_number, amount, password):
        account=self.get_account(account_number)
        if account:
            return account.withdraw(amount, password)
        else:
            return False

    def transfer(self, source_account, amount, password, target_account):
        source=self.get_account(source_account)
        target=self.get_account(target_account)
        if source and target:
            if source.withdraw(amount,password):
                return target.deposit(amount)

        return False

    def get_balance(self, account_number, password):
        account=self.get_account(account_number)
        if account is not None and account.authenticate(password):
            return account._balance
        else:
            return None


    def credit_interest(self):
        for account in self._accounts:
            account.credit_interest(self.interest_rate)


    def get_account_list(self):
        str=''
        for account in self._accounts:
            str+=f'{account}\n'

        return str

