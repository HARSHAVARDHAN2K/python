from banking.bank import Bank
from banking.atm import ATM


def get_bank():
    bank=Bank('ICICI',12)
    #add dummy account to the bank
    acc_type = input("ENTER the type of account you want to open")
    bank.open_account(acc_type,'Sanjay','p@ss',500000)
    bank.open_account(acc_type,'Prabhat','p@ss',500000)
    bank.open_account(acc_type,'Fagun','p@ss',500000)
    return bank


def main():
    bank=get_bank()
    # print(bank)

    atm=ATM(bank)

    # atm.start()
    # print('ATM shutdown')

if __name__=='__main__':
    main()