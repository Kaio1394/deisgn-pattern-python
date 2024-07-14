

from country import Country
from england_factory import EnglandFactory
from international_provider import InternacionalProvider


country = Country.ENGLAND
instance = InternacionalProvider.create(country)
print(f"{instance.__class__.__name__}")
