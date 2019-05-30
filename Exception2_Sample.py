""" Here, we are going to use LOOKUPERROR, which is a parent class for INDEXERROR OR KEYERROR exceptions.
Helps us to understand inheritance within Exception handling logic """


class Exception_Hierarchy:

    def lookup_hierarchy(self):
        sample_list = [3, 7, 9, 12]
        try:
            item = sample_list[5]
        except IndexError:
            print("Handling IndexError")

        sample_dict = dict(a=65, b=66, c=67)
        try:
            get_value = sample_dict['x']
        except KeyError:
            print("Handling KeyError")

code_eval = Exception_Hierarchy()
code_eval.lookup_hierarchy()
