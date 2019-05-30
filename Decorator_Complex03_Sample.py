""" Complex decorator functions """


from functools import wraps


def check_non_negative(index):
    def validate(passed_function):
        def wrap(*args, **kwargs):
            if args[index] < 0:
                raise ValueError("Arugment {} must be non-negative".format(index))
            return passed_function(*args)
        return wrap
    return validate


@check_non_negative(1)
def create_list(value, size):
    return [value] * size

print(create_list('Hey', 3))
print(create_list('Hey', -6))

