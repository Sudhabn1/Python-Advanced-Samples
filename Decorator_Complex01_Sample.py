""" Few complex decorator samples """

from functools import wraps


def base_function(passed_function):
    @wraps(passed_function)
    def inner_function(*args, **kwargs):
        print("Running the inner function!")
        if not can_run:
            return "Function will not run!"
        return passed_function(*args, **kwargs)
    return inner_function


@base_function
def generic_function():
    return "Function is running!"

can_run = True
print(generic_function())