from abc import ABC

from capital_city import CapitalCity
from language import Language


class InternationalFactory(ABC):
    @classmethod
    def create_language(self) -> Language:
        pass

    @classmethod
    def create_capital(self) -> CapitalCity:
        pass