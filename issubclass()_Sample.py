""" Python issubclass() Code """


class BaseClass:

    def __init__(self, num):
        print("Base Class")


class ChildClass(BaseClass):

    def __init__(self, num):
        super().__init__(num)
        print("Child Class")

eval_code = ChildClass(8)
print(type(eval_code))
print(eval_code.__repr__())
print(eval_code.__module__)
print(issubclass(ChildClass, BaseClass))
print(isinstance(eval_code, tuple))
