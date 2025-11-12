accounts = []
num_accounts = int(input("Enter number of bank accounts to create : "))

for i in range(num_accounts):
    print(f" Creating Account {i+1} ")
    name = input("Enter account holder name : ")
    balance = float(input("Enter initial balance : "))
    accounts.append([name, balance])
while True:
    print("           Bank Operations Menu           ")
    print("1. Display all account balances")
    print("2. Deposit to account")
    print("3. Withdraw from account")
    print("4. Display accounts above average balance")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5) : ")
    
    if choice == '1':
        print("      All Account Balances     ")
        for account in accounts:
            print(f"{account[0]}: {account[1]}")
    
    elif choice == '2':
        account_name = input("Enter account holder name for deposit : ")
        found = False
        for account in accounts:
            if account[0] == account_name:
                amount = float(input("Enter deposit amount : "))
                account[1] += amount
                print(f"Deposited {amount} to {account_name}")
                found = True
                break
        if not found:
            print(f"Account with name {account_name} not found")
    
    elif choice == '3':
        account_name = input("Enter account holder name for withdrawal : ")
        found = False
        for account in accounts:
            if account[0] == account_name:
                amount = float(input("Enter withdrawal amount : "))
                if amount <= account[1]:
                    account[1] -= amount
                    print(f"Withdrew {amount} from {account_name}")
                else:
                    print("Insufficient balance")
                found = True
                break
        if not found:
            print(f"Account with name {account_name} not found")
    
    elif choice == '4':
        total_balance = 0
        for account in accounts:
            total_balance += account[1]
        average_balance = total_balance / len(accounts)
        
        print(f"\nAverage balance : {average_balance}")
        print("    Accounts above average balance    ")
        
        for account in accounts:
            if account[1] > average_balance:
                print(f"{account[0]}: {account[1]}")
    
    elif choice == '5':
        print("Thank you for using the banking system!")
        break
    
    else:
        print("Invalid choice")