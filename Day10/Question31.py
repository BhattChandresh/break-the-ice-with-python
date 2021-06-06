# Question:
# Define a function which can print a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.


# Empty dictionary can be created by below methods.

my_dict = dict()  # OR


# my_dict = {}


print(" -- Method-1 -- ")
def square_it():
    print("....")
    for num in range(1, 21):
        my_dict[num] = num ** 2


def print_dictionary():
    square_it()
    for key, value in my_dict.items():
        print(str(key) + " -> " + str(value))


print_dictionary()


print(" -- Method-2 -- ")
def print_dictionary_method2():
    my_dict1 = {num: num ** 2 for num in range(1, 21)}
    print(my_dict1)


print_dictionary_method2()
