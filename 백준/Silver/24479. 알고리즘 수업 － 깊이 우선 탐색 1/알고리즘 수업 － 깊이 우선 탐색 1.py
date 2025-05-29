import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,k = map(int, input().rstrip().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)
for i in range(m): #6번
    x,z = map(int, input().rstrip().split())
    graph[x].append(z)
    graph[z].append(x)
for i in range(n+1):
    graph[i].sort()
a = 1
def dfs(start):
    visited[start] = True
    global a
    result[start] = a
    a += 1
    
    for i in graph[start]:    
        if not visited[i]: 
            dfs(i)


dfs(k)
for i in result[1:]:
    print(i)