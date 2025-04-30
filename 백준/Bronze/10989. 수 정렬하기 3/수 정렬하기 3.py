import sys
input=sys.stdin.readline
how = int(input().rstrip())
clist = [0]*10001
for i in range(how):
    clist[int(input().rstrip())] += 1
for i in range(len(clist)): #2
    for j in range(clist[i]):
        print(i)