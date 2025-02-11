from abc import ABC, abstractmethod
from datetime import datetime


class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount: float):
        """This is the how the payment will process"""
        pass


class CreditCardPayment(PaymentMethod):
    """This is for people who use credit card for the payment"""

    def __init__(
        self,
        card_number: int,
        cvv: int,
        expiry_date: datetime | str,
    ):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date

    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ₹ {amount}...")
        print(
            f"Card Number: {str(self.card_number)[-4]}, Expiry Date: {self.expiry_date}..."
        )
        print(f"Payment Successful 🍌")


class PayPalPayment(PaymentMethod):

    def __init__(self, email: str) -> None:

        self.email = email

    def process_payment(self, amount: float):
        print(f"Processing the payment of ₹{amount} from paypal...")
        print(f"Payment is using the email: {self.email.upper()}")
        print(f"Payment Successful 🍌")


class UpiPayment(PaymentMethod):

    def __init__(self, upi_id: str) -> None:
        """I am using the .lower() so that i can get unique all time"""
        self.upi_id = upi_id.lower()

    def process_payment(self, amount: float):
        print(f"Making a payment of ₹ {amount} from Indian UPI app.")
        print(f"Payment using the {self.upi_id}")
        print(f"Payment Successful of ₹ {amount}")


class BankTransferPayment(PaymentMethod):

    def __init__(
        self,
        account_no: int,
        ifsc_code: str,
    ) -> None:
        self.account_no = account_no
        self.ifsc_code = ifsc_code

    def process_payment(self, amount: float):
        print(
            f"Banking Transfer of ₹{amount} whole number amount can be transferred using the bank."
        )
        print(f"This payment is using the: {self.account_no} & {self.ifsc_code}")
        print(f"Payment Complete...")


def checkout(payment_method: PaymentMethod, amount: int):
    print(f"--- Checkout for ₹{amount} Using: {payment_method.__class__.__name__}---")
    payment_method.process_payment(amount)


cc_payment = CreditCardPayment(1234123412341234, 123, "12/26")
paypal_payment = PayPalPayment("user@example.com")
upi_payment = UpiPayment("user@upi")
bank_payment = BankTransferPayment(9876543210, "SBIN0001234")

checkout(cc_payment, 1000)  # Credit Card Payment
checkout(paypal_payment, 500)  # PayPal Payment
checkout(upi_payment, 250)  # UPI Payment
checkout(bank_payment, 2000)  # Bank Transfer Payment
