""" Transposing tables / data within Python code """

from pprint import pprint as pp

# Declaring 2 list items
sunday = [12, 17, 19, 12, 16, 18, 22]
monday = [14, 19, 17, 13, 19, 11, 24]

print(type(sunday))
print(type(monday))

# Merge both the list and it's gets converted to tuple

for merged_value in zip(sunday, monday):
    print(merged_value)
print()
print("-----------------")
print(type(merged_value))


# Declare one more list and merge it again
tuesday = [14, 18, 19, 14, 16, 21, 23]


# Declare another list
daily_temp = [sunday, monday, tuesday]
print()
print("Printing daily_temp list values !")
print("-----------------")
print(type(daily_temp))
print(daily_temp)
print()


# Extended merge
for extended_merge in zip(sunday, monday, tuesday):
    print(extended_merge)


# Import pretty-print module
print()
for good_print in zip(*daily_temp):
        pp(good_print)


# Transpose table
transposed = list(zip(*daily_temp))
print()
print("Transposed Value")
print("**************************")
pp(transposed)
print(transposed.index((12, 14, 14)))
print(transposed.__getitem__(0))
