import sys
input= sys.stdin.readline
a = 0
bg = [[0]*100 for _ in range(100)]
how = int(input().rstrip())
for _ in range(how):
    x, y = map(int, input().rstrip().split())
    for i in range(10):
        for j in range(10):
            bg[99-y-i][x+j] = 1
for i in range(100):
    a += bg[i].count(1)
print(a)