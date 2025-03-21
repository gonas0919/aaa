import sys
input= sys.stdin.readline
num, how = map(int, input().rstrip().split())
list1 = [i for i in range(1,num+1)]
for _ in range(how):
    c1, c2 = map(int, input().rstrip().split()) # 1 2
    list1[c1-1:c2] = list1[c1-1:c2][::-1] #0 1
for i in list1:
    print(i, end= ' ')  