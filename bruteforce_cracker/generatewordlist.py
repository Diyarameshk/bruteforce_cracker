from itertools import product
import string

min_length = int(input("Enter minimum length of password : "))
max_length = int(input("Enter maximum length of password : "))
counter = 0
character = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
file_open = open("wordlist.txt" , "w")

for i in range(min_length ,max_length+1):
    for j in product(character,repeat = i):
        word = " ".join(j)
        file_open.write(word)
        file_open.write("\n")
        counter += 1

print("wordlist of {} passwords created " .format(counter))