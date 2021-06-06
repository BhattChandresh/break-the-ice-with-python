# Question:
# Define a function which can generate and print a list
# where the values are square of numbers between 1 and 20 (both included).

square_list = list()
# OR square_list = []

print(" -- Method-1 -- ")
def square_number_list():
    for number in range(1,21):
        square_list.append(number**2)

def print_list():
    square_number_list()
    print(square_list)

print_list()

print(" -- Method-2 -- ")
def print_square_number():
    square_list1 = [num**2 for num in range(1,21)]
    print(square_list1)

print_square_number()