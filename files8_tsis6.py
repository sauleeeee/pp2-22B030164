import os

path ='./8.txt'
if os.path.exists(path):
    if os.access(path, os.R_OK):
        os.remove(path)