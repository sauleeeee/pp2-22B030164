import string
import os
for i in string.ascii_uppercase:
    file_name = i + '.txt'
    #os.remove(file_name )
    # print (file_name)
    with open(file_name, 'w') as f:
         pass