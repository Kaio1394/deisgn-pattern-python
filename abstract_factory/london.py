

from capital_city import CapitalCity


class London(CapitalCity):
    def get_population(self) -> int:
        return 1_000_000

    def list_top_attractions(self) -> []:
        return ["Tower Bridge", "Buckingham Palace"]