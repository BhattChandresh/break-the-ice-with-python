# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

line = input()
my_dict = dict()
upper_case = 0
lower_case = 0
for item in line:
    if item.isupper():
        upper_case += 1
        my_dict['uppercase'] = upper_case
    elif item.islower():
        lower_case += 1
        my_dict['lowercase'] = lower_case

print(f"Upper case = {my_dict.get('uppercase')} and lower case = {my_dict.get('lowercase')}")
