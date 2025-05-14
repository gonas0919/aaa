import sys
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
    visited[v] = True
    global a
    result[v] += a
    a +=1
    for j in graph[v]:
        if not visited[j]:
            dfs(graph, j , visited)

dfs(graph,r,visited)
for i in result[1:]:
    print(i)