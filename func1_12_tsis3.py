def histogram(li):
    for i in li:
        for k in range(i):
            print('*',end='')
        print()
li=list(map(int,input().split()))
histogram(li)