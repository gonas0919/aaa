import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n , m ,r = map(int, input().rstrip().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(1,m+1):
    u,v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
result = [0] * (n+1)
for i in range(1,n+1):
    graph[i].sort()
a = 1
def dfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        b = queue.popleft()
        global a
        result[b] += a
        a +=1
        for j in graph[b]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

dfs(graph,r,visited)
for i in result[1:]:
    print(i)