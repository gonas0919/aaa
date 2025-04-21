import sys
input=sys.stdin.readline
list1 = list(input().rstrip())
list1.sort(reverse=True)
for i in list1:
    print(i, end='')
