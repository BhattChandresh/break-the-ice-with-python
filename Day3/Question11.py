# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
# then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

binary_numbers = input().split(",")
value = list()
for item in binary_numbers:
    if (int(item,2) % 5) == 0:
        value.append(item)
print(",".join(value))