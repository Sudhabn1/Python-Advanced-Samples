""" Decorators samples code """


from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        func(*args, **kwargs)
    return with_logging


@logit
def generic_function(x):
    print(x * x)

generic_function(3)
