import sys
from collections import deque
input = sys.stdin.readline
dq = deque()
left = 0
right = 0
how = input().rstrip()
for i in how:
    dq.append(i)
for _ in range(len(how)//2):
    left += int(dq.popleft())
    right += int(dq.pop())
if left == right:
    print('LUCKY')
else:
    print('READY')