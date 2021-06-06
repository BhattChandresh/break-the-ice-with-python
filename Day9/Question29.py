# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.

print("-- Simple Method --")
def strJoin(str1,str2):
    return str1 + str2

print(strJoin("Chandresh ", "Bhatt"))

print("-- Lambda Function --")
my_str = lambda str3, str4 : str3 + str4
print(my_str("Mital ","Bhatt"))