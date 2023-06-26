n,m=map(int, input("Please Enter Row Column\n").split())
arr=[]
output=[]
for i in range(n):
    arr1=list(map(int, input("Please Enter Element with space\n").split()))
    arr.append(arr1)
for i in range(m):
    sin=[]
    for j in range(n):
        new=arr[j][i]
        sin.append(new)
    output.append(sin)
print(output)