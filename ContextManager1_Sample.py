""" Sample code for Context Manager logic within Python """


class LoggingContextManager:

    def __enter__(self):
        print("Entering __enter__ block!")
        return "You are in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Right now in __exit__ block!")
        print("LoggingContextManager.__exit__({}, {}, {}))".format(exc_type, exc_val, exc_tb))
        return
