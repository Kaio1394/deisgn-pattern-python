from credit_card_payment import CreditCardPayment
from google_pay_payment import GooglePayPayment
from not_dynamic.enum.payment_method import PaymentMethod
from paypal_payment import PayPalPayment

class PaymentFactory:
    @staticmethod
    def create(payment_method: PaymentMethod):
        match payment_method:
            case PaymentMethod.CREDIT_CARD:
                return CreditCardPayment()
            case PaymentMethod.PAYPAL:
                return PayPalPayment()
            case PaymentMethod.GOOLGE_PAY:
                return GooglePayPayment()
            case _:
                raise ValueError(f"{payment_method} is not currently suported.")