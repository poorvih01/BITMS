name = str(input("Enter your name: "))
n=len(name)
for i in range(n):
    for j in range(n):
        if i==0  or  i==n or i == n-1 or i+j==n-1:
            print(name[j], end=' ')
        else:
            print(' ', end=' ')
    print()
if(((i==0 or i==n) and j>=0 and j<=n)or i+j==n-1):
    print(name)



