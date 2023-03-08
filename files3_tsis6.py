import os
path = './dir.txt'
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print('not exist')