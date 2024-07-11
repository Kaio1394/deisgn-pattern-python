from models.payment import Payment
from decimal import Decimal

class CreditCardPayment(Payment):
    def pay(self, amount: Decimal):
       print(f"Successfully paid {amount} to merchant using a Credit Card.")