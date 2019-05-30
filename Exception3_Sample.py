""" Sample python code for New Exceptions Payload concept """

import math


class TriangleError(Exception):

    def triangle_area(self, a, b, c):
        sides = a, b, c
        if sides[2] > sides[0] + sides[1]:
            raise TriangleError("Illegal Triangle", sides)
        p = (a + b + c) / 2
        a = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return a


triangle_calc = TriangleError()
triangle_calc.triangle_area(2, 4, 15)

