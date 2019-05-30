""" Sample code for Assertions Invariants logic """


class AssertionLogic:

    def modulus_four(self, n):
        r = n % 4
        if r == 0:
            print("Multiple of 4")
        elif r == 1:
            print("Remainder 1")
        elif r == 2:
            print("Remainder 2")
        elif r == 3:
            print("Remainder 3")
        else:
            assert False, "This should never happen!"


eval_code = AssertionLogic()
eval_code.modulus_four(4)
