import sys
from bisect import bisect_left,bisect_right
input=sys.stdin.readline
a = int(input().rstrip())
list1 = list(map(int, input().rstrip().split()))
list1.sort()
b = int(input().rstrip())
list2 = list(map(int, input().rstrip().split()))
for i in range(b):
    left = bisect_left(list1,list2[i])
    right = bisect_right(list1,list2[i])
    print(right-left, end=' ')