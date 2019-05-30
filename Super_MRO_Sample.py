""" Python code sample for Super() MRO scenario's """


class SimpleList:

    def __init__(self, items):
        print("Simple List __init__ Call")
        self.items = items

    def add(self, item):
        print("Simple List 'add' Call")
        self.items.append(item)

    def get_item(self, index):
        return self.items[index]

    def sort(self):
        return self.items.sort()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        print("Simple List __repr__ Call")
        return repr(self.items)


class SortedList(SimpleList):

    def __init__(self, items):
        super().__init__(items)
        print("Sorted List __init__ Call")
        self.items = items

    def add(self, item):
        super().add(item)
        print("Sorted List 'add' Call")
        self.items.append(item)

    def __repr__(self):
        super().__repr__()
        print("Sorted List __repr__ Call")
        return repr(self.items)


sl = SortedList([3, 8, 4])
sl.add(1)
print(repr(SortedList))
print(sl.__repr__)








