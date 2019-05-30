""" Extended Inheritance Logic """


class SimpleList:

    def __init__(self, items):
        self.items = items
        print("Base Class __init__() Level")

    def add(self, item):
        self.items.append(item)
        print("Base Class add() Level")

    def get_item(self, index):
        print("Base Class get_item() Level")
        return self.items[index]

    def sort(self):
        print("Base Class sort() Level")
        return self.items.sort()

    def len(self):
        print("Base Class len() Level")
        return self.items.len()

    def repr(self):
        print("Base Class repr() Level")
        print(self.items)
        return "Base Class repr() Output {}".format(self.items)


class SortedList(SimpleList):

    def __init__(self, items=()):
        super().__init__(items)
        self.sort()
        print("Child Class __init__() Level")

    def add(self, item):
        super().add(item)
        self.sort()
        print("Child Class add() Level")

    def repr(self):
        super().repr()
        print("Child Class repr() Level")
        print(list(self.items))


sl = SortedList([1, 4, 8, 2, 9])
print(type(sl))
print(sl.items)
print(repr(sl))
sl.add(5)
print(sl.items)
print(sl.get_item(2))





