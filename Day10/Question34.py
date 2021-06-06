# Question:
# Define a function which can generate a list
# where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

print(" -- Method-1 -- ")
def square_number_print_first5():
    square_list = []
    for number in range(1,21):
        square_list.append(number**2)
    for index in range(5):
        print(square_list[index])

square_number_print_first5()

print(" -- Method-2 -- ")
def square_number_print_first5_method2():
    square_list = [num**2 for num in range(1,21)]
    print(square_list[0:5])
    
square_number_print_first5_method2()