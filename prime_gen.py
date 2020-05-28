t=int(input())
for i in range(t):
    x = input().split()
    a=int(x[0])
    b=int(x[1])
    l=list(range(2,b+1))
    for j in l:
        for k in range(j**2,b+1):
            if k%j==0:
                try:
                    l.remove(k)
                except:
                    continue
    for j in l:
        if j>=a and j<=b:
            print(j,end=" ")
    print()
    