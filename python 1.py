n = int(input())
a = list(map(int,input().split()))
c = 0
i = 0
for j in a:
  i = j+i
  if i<0:
    c = c+1
    i = 0
print(c)
