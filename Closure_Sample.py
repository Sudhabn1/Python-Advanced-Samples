""" Closures maintain references to objects from earlier scope """


def enclosing():
    x = 'closing over'

    def secondary_enclosing():
        print(x)
    return secondary_enclosing


TestEnclosing = enclosing()
TestEnclosing()
print(TestEnclosing.__closure__)
