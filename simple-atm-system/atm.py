class ATM:
    def __init__(self, pin: str = "1234", balance: float = 10000.0):
        self.pin = pin
        self.balance = balance
        self.is_authenticated = False

    def authenticate(self, entered_pin: str) -> bool:
        """Authenticate user with PIN"""
        if entered_pin == self.pin:
            self.is_authenticated = True
            return True
        return False

    def check_balance(self) -> float:
        if not self.is_authenticated:
            raise PermissionError("Please authenticate first.")
        return self.balance

    def withdraw(self, amount: float) -> str:
        if not self.is_authenticated:
            raise PermissionError("Please authenticate first.")
        if amount <= 0:
            return " Invalid amount. Please enter a positive value."
        if amount > self.balance:
            return " Insufficient balance."
        
        self.balance -= amount
        return f" Withdrawal successful! ₹{amount:,.2f} withdrawn.\n   Remaining Balance: ₹{self.balance:,.2f}"

    def deposit(self, amount: float) -> str:
        if not self.is_authenticated:
            raise PermissionError("Please authenticate first.")
        if amount <= 0:
            return " Invalid amount. Please enter a positive value."
        
        self.balance += amount
        return f" Deposit successful! ₹{amount:,.2f} deposited.\n   New Balance: ₹{self.balance:,.2f}"