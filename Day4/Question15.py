# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

print("-- Method-1 --")
print("Enter a number : ")
number = input()
my_equation = "a+aa+aaa+aaaa"
math_equation = my_equation.replace("a", number)
my_list = math_equation.split("+")
result = 0
for item in my_list:
    result = result + int(item)
print(result)

print("-- Method-2 --")
print("Enter a number : ")
number1 = input()
my_sum = int(number1) + int(2 * number1) + int(3 * number1) + int(4 * number1)
print(my_sum)

# TODO:
# Implement this with reduce method.
