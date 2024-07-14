from abc import ABC, abstractmethod
from decimal import Decimal

class Payment(ABC):
    @classmethod
    def pay(self, amount: Decimal):
        pass