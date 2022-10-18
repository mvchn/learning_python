def print_balance(account):
    print(f"Debits: {account['debits']}")
    print(f"Credits: {account['credits']}")
    if account['fees'] < 0:
        print(f"Fees: {-account['fees']}\n")
    else:
        print(f"Fees: {account['fees']}\n")

    print('------------')

    if account['balance'] < 0:
        print(f"Balance: {-account['balance']}\n")
    else:
        print(f"Balance: {account['balance']}\n")


user1 = {
    'debits': 200,
    'credits': 300,
    'fees': 500,
    'balance': 600
}

print_balance(user1)
