from abc import ABC

class CapitalCity(ABC):
    @classmethod
    def get_population(self) -> int:
        pass

    @classmethod
    def list_top_attractions(self) -> []:
        pass