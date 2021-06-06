# Question:
# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them alphanumerically.



print("-- Method-1 --")
words = input()
my_set = set(words.split(" "))
my_list = list(my_set)
my_list.sort()
print(" ".join(my_list))

print("-- Method-2 --")
words = input().split(" ")
for item in words:
    if words.count(item) > 1:
        words.remove(item)
words.sort()
print(" ".join(words))
