def isPrime(x):
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d == 0:
        return False
    else: 
        return True
def isPrime2(x):
    d = 2
    li2=[]
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d == 0:
        return x

def filt(li):
    print(list(map(lambda x : isPrime2(x), li)))
    

filt([1, 3, 5,7, 20, 21])
