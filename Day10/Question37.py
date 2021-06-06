# Question:
# Define a function which can generate and print a tuple
# where the value are square of numbers between 1 and 20 (both included).

print(" -- Method-1 -- ")
def square_tuple_m1():
    square_tuple = ()
    list1 = []
    for item in range(1,21):
        list1.append(item**2)
    square_tuple = tuple(list1)
    print(square_tuple[:])

square_tuple_m1()

print(" -- Method-2 -- ")
def square_tuple_m2():
    square_tupel = tuple()
    list2 = list()
    list2 = [number**2 for number in range(1,21)]
    square_tupel = tuple(list2)
    print(square_tupel[:])

square_tuple_m2()