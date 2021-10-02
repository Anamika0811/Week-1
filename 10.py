def twosum(nums,target):
    i=0
    while i<len(nums):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                print(i,j)
        i+=1        

nums=[1,3,5,2]
target=6
twosum(nums,target)
  