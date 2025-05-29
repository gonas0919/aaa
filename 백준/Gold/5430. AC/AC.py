import sys
input = sys.stdin.readline
from collections import deque
how = int(input().rstrip())
for _ in range(how):
    cmd = input().rstrip()
    num = int(input().rstrip())
    arr = input().rstrip()
    if num == 0:
        my_dq = deque()
    else:
        my_dq = deque(map(str, arr[1:-1].split(',')))
    rev = False
    error = False
    for arr in cmd:
        if arr == 'R':
            rev = not rev
        elif arr == 'D':
            if my_dq:
                if rev == False:
                    my_dq.popleft()
                else:
                    my_dq.pop()
            else:
                error = True
                break
    if error:
        print('error')
    else:
        if rev == True:
            my_dq.reverse()
        print('['+','.join(my_dq)+']')
        
        
