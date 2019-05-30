""" Class objects as decorators """


class BaseClass:

    def __init__(self, f):
        print("Calling __init__ function")
        self.f = f
        print("**",f)
        self.count = 0

    def __call__(self, *args, **kwargs):
        print("Calling __call__ function")
        self.count += 1
        return self.f(*args, **kwargs)


@BaseClass
def test_class_decorator(name):
    print("Hello {}".format(name))


test_class_decorator("Ravi")
test_class_decorator("Suresh")
test_class_decorator(name='Ramesh')
print(test_class_decorator.count)
