import sys
input=sys.stdin.readline
how = int(input().rstrip())
location = list(map(int, input().rstrip().split()))
location.sort()
if how%2 == 0:
    print(location[how//2-1])
else:
    print(location[how//2])