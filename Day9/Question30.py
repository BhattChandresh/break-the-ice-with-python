# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

print("-- Simple Method --")

def get_maxlength_string(str1,str2):
    max_len_string = list()
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)

get_maxlength_string("Chandresh","Mital")
get_maxlength_string("Chandresh","Mital Bhatt")
get_maxlength_string("Mital","Rudra")

print("-- Lamda Expression --")

result = lambda str3,str4: print(max((str3,str4),key=len)) if len(str3) != len(str4) else print(str3 + "\n" + str4)

result("aaa","bbbb")
result("abababab","cc")
result("xyzabc","abcxyz")
