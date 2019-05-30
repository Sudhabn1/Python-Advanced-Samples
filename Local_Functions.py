""" Sample code for local functions within Python, follows LEGB rule"""


class DemoCode:

    def sample_fun(self):
        def local_fun():
            a = 'hello'
            b = ' world'
            return a + b
        x = 1
        y = 2
        return x + y, local_fun()


ValidateCode = DemoCode()
print(ValidateCode.sample_fun())

