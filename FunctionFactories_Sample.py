""" Function Factory - Function that returns new, specialized functions """

# Factory function takes some arguments, it then creates a local function which takes
# it's own arguments and also uses arguments passed to the factory. Combination of runtime function definition
# and closures makes this possible


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(3)
print(square(5))
print(square.__closure__)