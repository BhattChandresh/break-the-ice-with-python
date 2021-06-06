# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class MyString():
    def __init__(self):
        self.s=""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


my_input = MyString()
my_input.get_string()
my_input.print_string()

