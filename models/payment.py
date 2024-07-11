from abc import ABC, classmethod
from decimal import Decimal

class Payment(ABC):
    @classmethod
    def pay(self, amount: Decimal):
        pass