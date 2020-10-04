def open_account():
    print("A new account has made.")

def deposit(balance, money):    # Deposit
    print("The deposit has been completed.")
    return balance + money

def withdraw(balance, money):   # Withdraw
    if balance >= money:
        print("The withdraw has been completed.")
        print("Balance is {0}" .format(balance-money))
        return balance - money
    else:
        print("Failed to withdraw money.")
        print("Balance is {0}" .format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("Commission is {0}, and balance is {1}." .format(commission, balance))



