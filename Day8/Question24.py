# Question:
# Python has many built-in functions, and
# if you do not know how to use it, you can read document online or find some books.
# But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
# And add document for your own function.

print("-- Documentation about list --")
print(list.__doc__)

print()
print("-- Documentation about abs --")
print(abs.__doc__)
print()


def square(number):
    """
    Return the square value of the input number
    The input number must be an integer.
    """
    return number ** 2


print("-- Documentation about square --")
print(square(2))
print(square.__doc__)
