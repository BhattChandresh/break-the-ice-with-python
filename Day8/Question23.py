# Question:
# Write a method which can calculate square value of number.

print("Enter a number : ")
number = int(input())

print("-- Method-1 --")


def square_the_number():
    return number ** 2


print(square_the_number())

my_result = lambda my_number: my_number ** 2
print(my_result(number))
