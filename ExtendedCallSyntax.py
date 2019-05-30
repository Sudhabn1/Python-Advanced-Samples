""" Sample code for an Extended Call Syntax mechanism in Python """


def print_val(args1, args2, *args):
    print(args1)
    print(args2)
    print(args)

sample_pass = (1, 3, 5, 7)

print_val(*sample_pass)


def print_kwarg_values(red, green, **kwargs):
    print("r =", red)
    print("g=", green)
    print(kwargs)

sample_inject = {'red': 30, 'green': 40, 'blue': 50, 'yellow': 60}

print_kwarg_values(**sample_inject)
