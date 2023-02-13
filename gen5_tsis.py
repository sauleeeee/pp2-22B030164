def nums(n):
    while n>0:
        yield n
        n=n-1
        if n==0:
            break
n=int(input())
print(list(nums(n)))