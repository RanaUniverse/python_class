from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float):
        """Process the payment to give"""
        ...


class CreditCardPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Paid ₹{amount} using the credit card")


class PaypalPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Paid ₹{amount} from the paypal app.")


class UpiPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Giving ₹{amount} from Indian upi app")


payment1 = CreditCardPayment()
payment1.pay(1000)

payment2 = PaypalPayment()
payment2.pay(2000)

payment3 = UpiPayment()
payment3.pay(444)
