import sys
input=sys.stdin.readline
how = int(input().rstrip())
list1 = [list(map(str, input().rstrip().split())) for _ in range(how)]
list1.sort(key=lambda x: int(x[0]))
for x,y in list1:
    print(x, y)