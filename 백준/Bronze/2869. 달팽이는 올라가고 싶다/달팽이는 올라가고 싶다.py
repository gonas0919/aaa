import sys
input = sys.stdin.readline
A,B,V = map(int,input().rstrip().split())#2 1 5
if (V-B)%(A-B) != 0:
    print((V-B)//(A-B)+1)
else:
    print((V-B)//(A-B))