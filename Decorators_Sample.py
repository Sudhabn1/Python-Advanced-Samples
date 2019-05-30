""" By definition, a decorator is a function that takes another
    function as an argument and extends the behavior of the latter function without explicitly modifying it. """


def base_function(function_name):
    def inner_function():
        print("Inner Function Executed")
        function_name()
    return inner_function


@base_function
def external_function(a=1, b=2):
    print("External Function Executed")
    print(a + b)

external_function()
