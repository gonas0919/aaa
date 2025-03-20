import sys
input= sys.stdin.readline
b, how = map(int, input().rstrip().split())
list1 = [i for i in range(1,b+1)]
for _ in range(how):
    bn, bn2= map(int, input().rstrip().split())
    list1[bn-1], list1[bn2-1] = list1[bn2-1], list1[bn-1]
for i in list1:
    print(i, end=' ')
