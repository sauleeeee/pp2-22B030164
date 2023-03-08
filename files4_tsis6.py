import os
with open("test.txt","w") as f:
    f.write("1\n2\n3\n4")

with open("test.txt","r") as f:
    print( len(f.readlines()))