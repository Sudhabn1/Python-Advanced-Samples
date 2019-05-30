""" Property Tag code sample within Python """


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

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        self._celsius = celsius

    # Setting property within the code

    @property
    def celsius(self):
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


# Calls base_class methods/functions
print("**********************************")
chennai_vessel = ShippingContainer('CHN', 'clothes')
print(chennai_vessel.next_serial)
print(chennai_vessel)
print(chennai_vessel.contents)
print(chennai_vessel.bic)
print("**********************************")
print()
print()

#  This is an important aspect of the code,
#  where "create_with_items" class method is used and passed celsius value

print("**********************************")
vishaka_vessel = RefrigeratedShippingContainer.create_with_items('VSK', ['clothes', 'jute'], celsius=3.0)
print(vishaka_vessel.next_serial)
print(vishaka_vessel.bic)
print(vishaka_vessel.celsius)
print(vishaka_vessel.contents)
print(vishaka_vessel._make_bic_code('VIH', 1556))
print("**********************************")
print()
print()


print("**********************************")
mumbai_vessel = RefrigeratedShippingContainer.create_with_items('MUM', ['fish', 'water'], celsius=2.0)
print(mumbai_vessel)
print(mumbai_vessel.celsius)
print(mumbai_vessel.fahrenheit)
mumbai_vessel.fahrenheit = 10.5
print(mumbai_vessel.celsius)
print(mumbai_vessel.bic)
print(mumbai_vessel._make_bic_code('BOM', 2334))
print("**********************************")
print()

