""" Decorator sample code being executed """


from functools import wraps


def base_function(passed_function):
    @wraps(passed_function)
    def inner_function():
        print("Executing Inner Function")
        passed_function()
    return inner_function


@base_function
def generic_function():
    print("Hey, I am a generic function!")

generic_function()
print(generic_function.__closure__)
print(generic_function.__code__)
print(generic_function.__name__)
