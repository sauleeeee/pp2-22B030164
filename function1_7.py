def has_33():
    flag=False
    nums=list(map(int,input().split()))
    # print(nums)
    for i in range(1, len(nums)):
        if nums[i]==3 and i+1!=len(nums) and nums[i+1]==3:
            flag=True
            break
    if flag:
        print('True')
    else:
        print('False')
has_33()


