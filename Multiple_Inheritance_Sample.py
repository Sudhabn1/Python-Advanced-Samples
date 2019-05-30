""" Python Code - Multiple Inheritance """


class FirstBaseClass:

    def __init__(self, num):
        print("First Base Class")


class SecondBaseClass:

    def __init__(self, num):
        print("Second Base Class")


class ChildClass(FirstBaseClass, SecondBaseClass):

    def __init__(self, num):
        print(FirstBaseClass.mro())
        print(SecondBaseClass.mro())
        FirstBaseClass.__init__(self, num)
        SecondBaseClass.__init__(self, num)
        print("Child Class")


child_object = ChildClass(8)
print(ChildClass.__bases__)
print(ChildClass.__base__)
print(child_object.__class__)
print(id(child_object))
print(child_object.__repr__())
print(ChildClass.__mro__)

