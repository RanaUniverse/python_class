class BankAccount:

    def __init__(
        self,
        account_holder: str,
        balance: float,
    ) -> None:
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = "1234"

    def deposit(
        self,
        amount: float,
    ):
        """Deposite some money into the account"""
        self._balance += amount
        print(
            f"Deposited ₹{amount} to {self.account_holder.upper()}, "
            f"New Balance: ₹{self._balance}"
        )

    def withdraw(self, amount: float, pin: str):
        """Withdraw money from the account with correct PIN"""
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print(
                    f"Withdraw {amount} from {self.account_holder.upper()} "
                    f"Remaining Balance: ₹{self._balance}"
                )
            else:
                print(f"Insufficient Balance😢. Remaining: ₹{self._balance}")
        else:
            print(f"Incorrect PIN: {pin} ❌")

    def get_balance(self, pin: str):
        if pin == self.__pin:
            return (
                f"Current Balance of {self.account_holder.upper()} is: ₹{self._balance}"
            )
        else:
            return "Incorrect PIN ❌"


a1 = BankAccount("Rahul Jana", 500)

print(a1.get_balance("1234"))

a1.deposit(999)

print(a1.get_balance("1234"))

a1.withdraw(7000, "1234")
print(a1.get_balance("1234"))
