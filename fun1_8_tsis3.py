def spy_game():
    # flag=False
    # nums=list(map(int,input().split()))
    # # print(nums)
    # for i in range(1, len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i]==0 and nums[j]==0 and nums[j+1]==7 :
    #             flag= True
    #         break
    # if flag:
    #     print('True')
    # else:
    #     print('False')
    nums=list(map(int,input().split()))
    flag=False
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]==0 and nums[j]==0 and nums[k]==7 :
                    flag= True
                    break
    if flag:
        print('True')
    else:
        print('False')

spy_game()