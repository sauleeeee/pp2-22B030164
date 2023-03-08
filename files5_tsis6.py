#Write a Python program to write a list to a file.
import os
mylist = ['My', 'Name', "is", "Saule"]

with open("text.txt", "w") as f:
    for i in range(len(mylist)):
        f.write(mylist[i] + ' ')
        print("done")