""" Sample code for str() and repr() logic within Python """


class Point2D:

    def __init__(self, x, y):
        print("Running Code!")
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

validate_code = Point2D(20, 30)
print(validate_code.__str__())
print(validate_code.__repr__())
