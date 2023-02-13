def even(a):
    for i in range(1,a+1):
        if i % 2 == 0:
            yield i
    
a=int(input())  
for i in even(a):
    if i != a:
        print(i,end=",")
    else:
        print(i)
