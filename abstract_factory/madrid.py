

from capital_city import CapitalCity


class Madrid(CapitalCity):
    def get_population(self) -> int:
        return 100_000

    def list_top_attractions(self) -> []:
        return ["Roayal Palace", "Prado Museum"]