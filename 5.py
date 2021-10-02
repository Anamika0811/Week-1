arr=[4,6,13,12,15]
N=5
X=int(input("Enter the number X: "))
for i in range(N):
    for j in range(0,N-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for k in range(0,N):
    if X==arr[k]:
        print(arr[k-1]) 

