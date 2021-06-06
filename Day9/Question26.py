# Question:
# Define a function which can compute the sum of two numbers.

print(" -- Simple Method --")
def add_numbers(number1,number2):
    return number1 + number2

print("SUM is = ", add_numbers(5,5))
print("SUM is = ", add_numbers(10.3,10.5))


print(" -- Using Lamda --")
result = lambda number3, number4 : number3 + number4

print(result(10,20))
print(result(10.4,11.2))


