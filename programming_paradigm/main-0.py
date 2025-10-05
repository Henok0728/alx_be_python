import sys
import json
from bank_account import BankAccount

BALANCE_FILE = "balance.json"

def load_balance():
    try:
        with open(BALANCE_FILE, "r") as f:
            data = json.load(f)
            return data.get("balance", 0.0)
    except FileNotFoundError:
        return 100.0  

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        json.dump({"balance": balance}, f)

def main():
    account = BankAccount(load_balance())

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    parts = sys.argv[1].split(":")
    command = parts[0].lower()
    amount = float(parts[1]) if len(parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

    save_balance(account.account_balance)

if __name__ == "__main__":
    main()
