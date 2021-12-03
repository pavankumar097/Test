n,k = map(int,input().split())
c = 0
for i in range(n):
    a = input()
    b = 0
    for j in range(k+1):
        if str(j) in a:
            b = b+1
    if b == k+1:
        c = c+1
print(c)
