# Question:
# Define a function that can convert a integer into a string and print it in console.

print(" -- Simple Method --")
def intToStr(number):
    return str(number)

print(intToStr(15))


print(" -- Lamda Expression --")
intToStr1 = lambda my_number: str(my_number)
my_string = intToStr1(30)
print(my_string)
print(type(my_string))
