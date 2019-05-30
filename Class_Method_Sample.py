""" Class method code sample used in Python """


class ShippingOrg:

    shipping_vessel_number = 1993

    # Class Method
    @classmethod
    def _shipping_vessel_number_allocation(cls):
        result = cls.shipping_vessel_number
        cls.shipping_vessel_number += 5
        return result

    # Named Constructors are also known as Factory Functions, which requires class to support
    @classmethod
    def empty_container(cls, owner_code):
        return cls(owner_code, contents=None)

    # Generic Function
    def process_shipping_values(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingOrg._shipping_vessel_number_allocation()
        return owner_code, contents


clothing_vessel = ShippingOrg()
veg_vessel = ShippingOrg.empty_container('NOQ')  # Another way of calling constructor alone!
print(veg_vessel)

print(clothing_vessel.process_shipping_values('ABN', 'clothes'))
print(clothing_vessel.shipping_vessel_number)


