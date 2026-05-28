n=5
for i in range(1,n):
    for j in range(i):
        print("*",end=" ")
    print()
for k in range(1,n-1):
    for l in range(n-1,k,-1):
        print("*",end=" ")
    print()


