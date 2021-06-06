# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

my_input = input().split(",")
my_list = list(my_input)
my_tuple = tuple(my_input)

print(my_list)
print(my_tuple)