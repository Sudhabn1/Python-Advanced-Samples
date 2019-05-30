""" Static method code sample with a decorator """


class Cargo:

    cargo_number = 1993

    @staticmethod
    def _cargo_number_calculation():
        result = Cargo.cargo_number
        Cargo.cargo_number += 2
        return result

    def process_cargo(self, owner_code, contents):
        print("Printing Owner Code =", owner_code)
        print("Printing Contents =", contents)
        cargo_number = Cargo._cargo_number_calculation()
        print("Printing Cargo Number =", cargo_number)


print(Cargo.cargo_number)
Ship_Cargo = Cargo()
Ship_Cargo.process_cargo('ABN', 'clothes')

Shipping_Org = Cargo()
Shipping_Org.process_cargo('CUV', 'gadgets')
