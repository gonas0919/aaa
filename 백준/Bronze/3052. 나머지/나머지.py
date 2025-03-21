import sys
input= sys.stdin.readline
set1 = set(int(input().rstrip())%42 for _ in range(10))
print(len(set1))
