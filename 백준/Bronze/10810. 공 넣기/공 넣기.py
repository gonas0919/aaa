N , M = map(int, input().split())
a = [0]*N
for p in range(M):
    i , j ,k = map(int, input().split())
    for x in range(i,j+1):
        a[x-1] = k

for t in range(N):
    print(a[t], end=' ')