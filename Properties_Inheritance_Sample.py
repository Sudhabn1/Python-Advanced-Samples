""" Code showcasing Inheritance model via Properties """

from ComplexPythonSamples import iso6346


class ShippingContainer:

    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, *args, contents=None, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def __init__(self, owner_code, contents, length_ft, celsius):
        super().__init__(owner_code, length_ft, contents)
        self._celsius = celsius

    # Setting property within the code

    @property
    def celsius(self, value):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

#  Rather than writing ShippingContainer.HEIGHT_FT or ShippingContainer.WIDTH_FT, you can use super() function
    @property
    def volume_ft3(self):
        return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT


chennai_vessel = ShippingContainer.create_empty('CHN', 20)
print(chennai_vessel)
print(chennai_vessel.volume_ft3)

mumbai_vessel = RefrigeratedShippingContainer('MUM', 'rice', 15, celsius=2.0)
print(mumbai_vessel)
print(mumbai_vessel.volume_ft3)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temp out of range !")
        RefrigeratedShippingContainer.celsius.fset(self, value)

vishaka_vessel = HeatedRefrigeratedShippingContainer('VSK', 'fish', 20, celsius=-2.0)
print(vishaka_vessel.volume_ft3)
print(vishaka_vessel.FRIDGE_VOLUME_FT)
