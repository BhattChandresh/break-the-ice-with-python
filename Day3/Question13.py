# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.

line = input()
my_dict = dict()
digit = 0
letter = 0
for item in line:
    if item.isdigit():
        digit += 1
        my_dict['digits'] = digit
    elif item.isalnum():
        letter += 1
        my_dict['letters'] = letter

print("Digits = ", my_dict.get('digits'))
print("Letters =", my_dict.get('letters'))