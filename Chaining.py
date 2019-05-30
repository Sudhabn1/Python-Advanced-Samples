""" Sample code for Explicit Exceptions within Python logic """

import math

class InclinationError(Exception):


    def inclination(self, dx, dy):
        try:
            return math.degrees(math.atan(dy / dx))
        except ZeroDivisionError as e:
            print("Printing e", e)
            print("Printing __cause__", e.__cause__)
            print("Printing __trace__", e.__traceback__)
            raise InclinationError("Slope cannot be vertical") from e


eval_code = InclinationError()
eval_code.inclination(0, 5)


