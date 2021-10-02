array=[5,7,7,8,8,10]
target=8
pos=[]
for i in range(0,len(array)):
    if array[i]==target:
        pos.append(i)
print(pos[0],pos[-1])        