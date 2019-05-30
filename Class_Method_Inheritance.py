""" Inheritance with Class methods """

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
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R')

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too hot!")
        self.celsius = celsius


chennai_vessel = ShippingContainer('CHN', 'clothes')
print(chennai_vessel)
print(chennai_vessel.contents)
print(chennai_vessel.bic)

#  This is an important aspect of the code,
#  where "create_with_items" class method is used and passed celsius value

vishaka_vessel = RefrigeratedShippingContainer.create_with_items('VSK', ['clothes', 'jute'], celsius=3.0)
print(vishaka_vessel.bic)
print(vishaka_vessel.celsius)
print(vishaka_vessel._make_bic_code('VIH', 1556))

# If you make modifications to __init__ file, it makes a difference
# Keep a close watch on this code
