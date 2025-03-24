import sys
input= sys.stdin.readline
A = list(map(int, input().rstrip().split()))
print(A[1]*2-A[0])