# Question:
# Define a function that can receive two integer numbers in string form
# and compute their sum and then print it in console.

print(" -- Simple Method --")
def add_numbers(str1, str2):
    return (int(str1) + int(str2))

print(add_numbers('15','10'))


print(" -- Lamda Function --")
add_numbers1 = lambda str3,str4 : int(str3) + int(str4)
result = add_numbers1('15','10')
print(result)
print(type(result))
