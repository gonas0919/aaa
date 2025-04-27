import sys
input = sys.stdin.readline
how = int(input().rstrip())
list1 = []
for i in range(0,1167):
    for j in range(1,1001):
        if (3*i)+(5*j) == how:
            list1.append(i+j)

for i in range(0,1001):
    for j in range(1,1167):
        if (3*j)+(5*i) == how:
            list1.append(i+j)

if len(list1) == 0:
    print(-1)
else:
    print(min(list1))
