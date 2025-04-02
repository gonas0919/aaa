import sys
import queue
input = sys.stdin.readline
q= queue.Queue()
how = int(input().rstrip())
for _ in range(how):
    ask = input().split()
    if ask[0] == 'push':
        q.put(ask[1])
    elif ask[0] == 'pop':
        if q.qsize() == 0:
            print(-1)
        else:
            print(q.get())
    elif ask[0] == 'size':
        print(q.qsize())
    elif ask[0] == 'empty':
        if q.qsize() == 0:
            print(1)
        else:
            print(0)
    elif ask[0] == 'front':
        if q.qsize() >= 1:
            print(q.queue[0])
        if q.qsize() == 0:
            print(-1)
    elif ask[0] == 'back':
        if q.qsize() >= 1:
            print(q.queue[-1])
        if q.qsize() == 0:
            print(-1)