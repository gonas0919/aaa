import sys
input=sys.stdin.readline
how = int(input().rstrip())
list1 = []
for _ in range(how):
    a = list(map(int, input().rstrip().split()))
    list1.append(a)

list1.sort()
for x, y in list1:
    print(x, y)