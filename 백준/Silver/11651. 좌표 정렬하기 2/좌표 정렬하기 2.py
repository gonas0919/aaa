import sys
input=sys.stdin.readline
how = int(input().rstrip())
list1 = []
for _ in range(how):
    a = list(map(int, input().rstrip().split()))
    list1.append(a)
for i in range(how):
    list1[i][0], list1[i][1] = list1[i][1], list1[i][0]
list1.sort()
for i in range(how):
    list1[i][0], list1[i][1] = list1[i][1], list1[i][0]
for x,y in list1:
    print(x,y)