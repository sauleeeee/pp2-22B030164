#Write a Python program to copy the contents of a file to another file
import os
with open('test.txt', 'r') as f:
    content = f.read()

with open('output.txt', 'w') as k:
    k.write( content )
    