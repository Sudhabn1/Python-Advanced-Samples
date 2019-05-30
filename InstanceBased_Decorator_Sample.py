""" Instance as Decorators """


class BaseClass:

    def __init__(self):
        print("Calling __init__ Function")

    def __call__(self, invoked_function):
        def say_hello(*args, **kwargs):
            print("Running say_hello Function")
            return invoked_function(*args, **kwargs)
        return say_hello

instanceObject = BaseClass()


@instanceObject
def validate_code(name):
    print("Hello {}".format(name))


validate_code("Ram")
