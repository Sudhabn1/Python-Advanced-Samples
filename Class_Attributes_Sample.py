""" Sample code speaking about class attributes, cargo_number is a class attribute """


class ShippingContainer:

    cargo_number = 1991

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.cargo_number = ShippingContainer.cargo_number
        ShippingContainer.cargo_number += 2


print(ShippingContainer.cargo_number)
sc1 = ShippingContainer('ABO', 'gadgets')
print(sc1.owner_code)
print(sc1.contents)
print(sc1.cargo_number)

sc2 = ShippingContainer('XCU', 'clothes')
print(sc2.owner_code)
print(sc2.cargo_number)
print(sc2.contents)
