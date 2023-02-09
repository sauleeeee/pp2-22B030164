def prime(i):
    t=2
    while t<i:
        if i%t==0:
            return False
        t+=1
    return True


my_list=list(map(int,input().split()))
for i in my_list:
    if prime(i):
        print(i)
    else:
        continue
