from inspect import *
import models

class DynamicFactory(object):
    payment_dict = {}

    def __init__(self) -> None:
        self.load_payment_types()

    def load_payment_types(self):
        members = getmembers(models, lambda x: isclass(x) and not isabstract(x))
        for name, _type in members:
            if isclass(_type) and issubclass(_type, models.payment.Payment):
                self.payment_dict[name] = _type

    def create(self, payment_type: str):
        if payment_type in self.payment_dict:
            return self.payment_dict[payment_type]()
        else:
            raise ValueError(f"{payment_type} is not currently suported.") 