import sys
input=sys.stdin.readline
a,b,c,d,e,f = map(int, input().rstrip().split())
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i+b*j == c and d*i+e*j==f:
            print(i,j)