""" Static Method Inheritance """

from ComplexPythonSamples import iso6346


class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R')

chennai_vessel = ShippingContainer('CHN', 'clothes')
print(chennai_vessel)
print(chennai_vessel.contents)
print(chennai_vessel.bic)

#  This is an important aspect of the code
vishaka_vessel = RefrigeratedShippingContainer('VSK', 1569)
print(vishaka_vessel._make_bic_code('VIS', 1344))  # Directly calling the static method to see changes
