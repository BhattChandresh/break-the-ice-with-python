# Question:
# Define a function which can generate a dictionary
# where the keys are numbers between 1 and 20 (both included) and
# the values are square of keys.
# The function should just print the keys only.

my_dict = {}


print(" -- Method-1 -- ")
def square_it():
    for num in range(1, 21):
        my_dict[num] = num ** 2


def print_keys():
    square_it()
    for k, v in my_dict.items():
        print(k)


print_keys()

print(" -- Method-2 -- ")
def print_dictionary_keys():
    my_dict1 = {num: num **2 for num in range(1,21)}
    print(my_dict1.keys())

print_dictionary_keys()