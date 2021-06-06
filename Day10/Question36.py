# Question:
# Define a function which can generate a list
# where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.

print(" -- Method-1 -- ")
def square_number():
    square_list = []
    for number in range(1,21):
        square_list.append(number**2)
    print(square_list[5:])

square_number()

print(" -- Method-2 -- ")
def square_number_m2():
    square_list = list()
    square_list = [item**2 for item in range(1,21)]
    print(square_list[5:])

square_number_m2()
