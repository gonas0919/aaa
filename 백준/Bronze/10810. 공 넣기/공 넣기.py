import sys
input= sys.stdin.readline
b, how = map(int, input().rstrip().split())
list1 = [0 for _ in range(b)]
for i in range(how):
    bn, bn2, num = map(int, input().rstrip().split()) # 1 3 5
    for i in range(bn,bn2+1): # 1 4
        list1[i-1] = num
for i in list1:
    print(i, end=' ')
