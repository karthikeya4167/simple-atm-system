from atm import ATM

def print_header():
    print("\n" + "="*45)
    print("           SIMPLE ATM SYSTEM")
    print("="*45)

def main():
    atm = ATM(pin="1234", balance=10000.0)

    print_header()
    print("Welcome! Default PIN is: 1234")
    print("-" * 45)

    # Authentication
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ").strip()
        if atm.authenticate(pin):
            print("\n Authentication Successful!\n")
            break
        attempts -= 1
        print(f" Incorrect PIN. Attempts remaining: {attempts}")
    else:
        print("\n Too many incorrect attempts. Card blocked.")
        return

    # Main Menu
    while True:
        print("\n" + "-"*30)
        print("           ATM MENU")
        print("-"*30)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        print("-"*30)

        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == "1":
                balance = atm.check_balance()
                print(f"\n Your Current Balance: ₹{balance:,.2f}")

            elif choice == "2":
                amount = float(input("Enter amount to withdraw: ₹"))
                print("\n" + atm.withdraw(amount))

            elif choice == "3":
                amount = float(input("Enter amount to deposit: ₹"))
                print("\n" + atm.deposit(amount))

            elif choice == "4":
                print("\n Thank you for using Simple ATM. Goodbye!")
                break

            else:
                print(" Invalid choice. Please try again.")

        except ValueError:
            print(" Please enter a valid number.")
        except PermissionError as e:
            print(f" {e}")

if __name__ == "__main__":
    main()