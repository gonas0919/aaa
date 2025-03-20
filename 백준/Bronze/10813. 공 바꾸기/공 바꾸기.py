N , M = map(int, input().split())
a = []
for x in range(1,N+1):
    a.append(x)
for p in range(M):
    i, j = map(int, input().split())
    a[i-1] , a[j-1] = a[j-1] , a[i-1]
for h in a:
    print(h,end = ' ')