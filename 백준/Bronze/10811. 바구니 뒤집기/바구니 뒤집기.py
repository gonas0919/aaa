n,m = map(int, input().split())
a = []
a1 = []
for b in range(1,n+1):
    a.append(b)
for p in range(m):
    i , j = map(int, input().split())
    a1 = a[i-1:j]
    a1.reverse()
    a[i-1:j] = a1
for y in range(n):
    print(a[y], end=' ')