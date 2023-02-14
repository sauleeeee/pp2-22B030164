def square(a):
    for i in range(1,a):
        yield i*i
a=int(input())
print(list(square(a)))