import sys
input=sys.stdin.readline
num = int(input().rstrip())

for i in range(1,num+1):
    sev = str(i)
    sev1 = [int(x) for x in sev]
    a = 0
    if int(sev) + sum(sev1) == num:
        a = int(sev)
        print(a)
        break
if a == 0:
    print(0)