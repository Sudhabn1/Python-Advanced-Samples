""" Few samples of Iterables and Iteration logic within Python """

# Comprehensions - Few samples!
from functools import reduce

sample_range = range(100)
print(sample_range)
conv_list = list(sample_range)
print(conv_list)

sample_comp = [x * 2 for x in range(10)]
print(sample_comp)

print([(x, y) for x in range(5) for y in range(3)])

sample_output = [[x, y] for x in range(10) for y in range(x)]
print(sample_output)

nc = [[x * 2 for x in range(10)] for y in range(5)]
print(nc)


# map() coding samples

map_out = map((x * 2 for x in range(10)), (y * 5 for y in range(10)))
print(type(map_out))

color = ['white', 'black', 'red', 'blue']
fruits = ['apple', 'mango', 'banana', 'papaya']
cities = ['bangalore', 'mysore', 'bidar', 'hubli']


def combine(color, fruits, cities):
    return '{}, {}, {}'.format(color, fruits, cities)

common_map = map(combine, color, fruits, cities)
output_to_list = list(common_map)
print(output_to_list.index('black, mango, mysore'))


# filter() coding sample
positives = filter(lambda x: x > 0, [1, -3, -22, 22, 80, -36])
print(list(positives))


# functools.reduce() sample
def multiple(x, y):
    print("value {} {}".format(x, y))
    return x * y

reduce(multiple, range(1, 10))
print(reduce(multiple, [1]))


# Iterator & Iterable

class ExampleIterator:

    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3, 4, 5]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        result = self.data[self.index]
        self.index += 1
        return result

sample_obj = ExampleIterator()
print(next(sample_obj))
print(next(sample_obj))
print(next(sample_obj))
print(next(sample_obj))
print(next(sample_obj))  # Beyond this print level, it will raise StopIteration error


# Both samples together

class ExIterator:

    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        result = self.data[self.index]
        self.index += 1
        return result


class ExIterable:

    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return ExIterator(self.data)

