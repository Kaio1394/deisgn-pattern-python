from country import Country
from england_factory import EnglandFactory
from international_factory import InternationalFactory
from spain_factory import SpainFactory

class InternacionalProvider:
    @staticmethod
    def create(country: Country) -> InternationalFactory:
        match country:
            case Country.ENGLAND:
                return EnglandFactory()
            case Country.SPAIN:
                return SpainFactory()
            case _:
                raise ValueError(f"This {country} is not currently supported.")