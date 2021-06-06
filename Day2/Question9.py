# Question:
# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.

my_list = []
while True:
    lines = input()
    if len(lines) == 0:
        break;
    my_list.append(lines)

for item in my_list:
    print(item.upper())
