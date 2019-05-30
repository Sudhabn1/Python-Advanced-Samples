""" Python code for isinstance() built-in function """


class BaseClass:

    def __init__(self, items):
        print("Base Class __init__ Level")
        self.items = items

    def add(self, item):
        print("Base Class add() Level")
        self.items.append(item)

    def repr(self):
        print("Base Class repr() Level")
        print(self.__repr__())


class ChildClass(BaseClass):

    def __init__(self, items=()):
        print("Child Class __init__ Level")
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("Only supports 'int' values !")

    def add(self, item):
        print("Child Class add() Level")
        self.items.append(item)

    def repr(self):
        super().repr()
        print("Child Class repr() Level")
        print(self.__repr__())


eval_code = ChildClass((2, 4, 6, 8))
eval_code.repr()








