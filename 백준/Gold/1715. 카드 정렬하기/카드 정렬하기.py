import sys
from queue import PriorityQueue
q = PriorityQueue()
input=sys.stdin.readline
how = int(input().rstrip())
for _ in range(how):
    q.put(int(input().rstrip()))
A = 0
while q.qsize()>1: 
    a = q.get()
    b = q.get()
    A += a+b
    q.put(a+b)
print(A)