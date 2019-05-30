""" Returning functions from a function, can be treated like an object """


def enclosing():
    def inner_func():
        print("Inner Function")
    return inner_func

ValidateLogic = enclosing()
ValidateLogic()

