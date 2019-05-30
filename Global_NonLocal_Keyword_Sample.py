""" Global & Nonlocal Keyword Sample """

message = "global"


def enclosing():
    message = 'enclosing'

    def local_func():
        global message
        message = 'local'

    print('1st Print =', message)
    local_func()
    print('2nd Print =', message)


print('3rd Print =', message)
enclosing()
print('4th Print =', message)


# ------------------------------------------------------
print()
print()
print()
val = "global"


def main_function():
    val = 'main_func_value'

    def child_function():
        nonlocal val
        val = 'child_func_value'

    print('1st Print =', val)
    child_function()
    print('2nd Print =', val)


print('3rd Print =', val)
main_function()
print('4th Print =', val)