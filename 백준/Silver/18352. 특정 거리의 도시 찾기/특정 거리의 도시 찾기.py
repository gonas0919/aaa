import sys
from collections import deque
input = sys.stdin.readline
n , m ,k,x = map(int, input().rstrip().split()) #개수, 도로개수, 몇만큼, 어디서부터
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
#인접한 좌표 리스트
for i in range(1,m+1):
    u,v = map(int, input().rstrip().split())
    graph[u].append(v)
#몇개의 간선을 지나야 하는지
result = [0] * (n+1)
#정렬하기
for i in range(1,n+1):  
    graph[i].sort()

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        b = queue.popleft()
        for j in graph[b]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                result[j] = result[b] + 1
            
bfs(graph,x,visited)
#구하고자 하는 간선만큼의 개수가 없으면 -1
if k not in result[1:]:
    print(-1)
#있으면 for문으로 인덱스 찾기. 찾은 값은 *로 변환
else:
    for i in result[1:]:
        if i == k:
            print(result.index(i))
            result[result.index(i)] = '*'
