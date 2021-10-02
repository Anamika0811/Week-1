def ismonotonic(nums):
    flag=True
    l=len(nums)
    for i in range(0,l):
        for j in range(i+1,l):
            if nums[i]>nums[j]:
                flag=False
    if flag:
        print("True") 
    else:
        print("False")

a=[1,2,3]
ismonotonic(a)                       
