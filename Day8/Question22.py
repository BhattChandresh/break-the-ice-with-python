# Question:
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

sentences = input()
my_dict = dict()
my_list = sentences.split(" ")
for item in my_list:
    my_dict[item] = my_list.count(item)
for words, count in sorted(my_dict.items()):
    print(f"{words}:{count}")
