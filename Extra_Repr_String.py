""" repr() and str() built-in code or logic sample """

import pdb

class ReprStr:

    def good_function(self):
        print("Invoking a generic function call")

    def __repr__(self):
        return "Code is running repr function!"

    def __str__(self):
        return "Code is running str function!"


validate = ReprStr()
validate.good_function()
print("repr - ", validate.__repr__())
print("str - ", validate.__str__())
print(pdb.getsourcelines(ReprStr))
