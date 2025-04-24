import sys
input=sys.stdin.readline
how = int(input().rstrip())
list1 = []
for _ in range(how):
    what = input().rstrip()
    if not what in list1:
        list1.append(what)
list1.sort()
list1.sort(key=len)

for i in list1:
    print(i)