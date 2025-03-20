import sys
input= sys.stdin.readline
how = input().rstrip()
list1 = list(map(int, input().rstrip().split()))
what = int(input().rstrip())
print(list1.count(what))