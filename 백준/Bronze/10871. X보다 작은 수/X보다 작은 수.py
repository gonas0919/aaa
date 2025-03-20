import sys
input= sys.stdin.readline
how, num= map(int, input().rstrip().split())
list1 = list(map(int, input().rstrip().split()))
for i in list1:
    if i<num:
        print(i, end=' ')