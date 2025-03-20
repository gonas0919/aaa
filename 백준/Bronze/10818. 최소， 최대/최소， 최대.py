import sys
input= sys.stdin.readline
how= int(input().rstrip())
list1 = list(map(int, input().rstrip().split()))
print(min(list1), max(list1))
