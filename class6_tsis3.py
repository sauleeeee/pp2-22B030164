def isPrime(x):
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d == 0:
        return False
    else: 
        return True
def filt(li):
    # print(list(map(lambda x : isPrime(x), li)))
    print(list(filter(isPrime, [1, 3, 5,7 , 20, 21])))

filt([1, 3, 5,7, 20, 21])