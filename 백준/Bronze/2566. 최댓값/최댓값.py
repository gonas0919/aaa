a = []
for i in range(9):
    a1 = list(map(int, input().split()))
    a.append(a1)
a2 = list(map(max, a))
print(max(a2))
print(a2.index(max(a2))+1 ,a[a2.index(max(a2))].index(max(a2))+1)