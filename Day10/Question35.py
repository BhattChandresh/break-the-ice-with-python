# Question:
# Define a function which can generate a list
# where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

print(" -- Method-1 -- ")
def square_numbers_list():
    square_list = list()
    for number in range(1,21):
        square_list.append(number**2)
    print(square_list[-5:])

square_numbers_list()

print(" -- Method-2 -- ")
def square_number_list_m2():
    square_list = []
    square_list = [number**2 for number in range(1,21)]
    for item in range(19,14,-1):
        print(square_list[item])

square_number_list_m2()