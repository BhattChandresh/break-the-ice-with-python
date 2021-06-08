# Question:
# write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

print("-- Method-1 Using filter --")

input_list = [5, 6, 77, 45, 22, 12, 24]


def iseven(number):
    return number % 2 != 0


my_list1 = list(filter(iseven, input_list))
print(my_list1)

print("-- Method-2 Using Comprehension --")

my_list2 = [element for element in input_list if element % 2 != 0]
print(my_list2)
