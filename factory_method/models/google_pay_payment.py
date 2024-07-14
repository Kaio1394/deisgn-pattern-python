from models.payment import Payment
from decimal import Decimal

class GooglePayPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid {amount} to merchant using a GooglePay.")