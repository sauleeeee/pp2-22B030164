lis= []
lis = input()
upp = 0
low = 0
for i in lis:
    
    if i.isupper():
        upp +=1
    elif i.islower():
        low +=1
print(upp,low, sep=" ")
