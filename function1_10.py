def unique(li):
    linew=[]
    for i in li:
        if i not in linew:
            linew.append(i)
    return linew
li=list(map(int,input().split()))
print(unique(li))