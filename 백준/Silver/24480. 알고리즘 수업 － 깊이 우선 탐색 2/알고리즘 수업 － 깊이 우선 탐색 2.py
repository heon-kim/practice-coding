import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n):
    global count
    visited[n] = count
    count += 1
    for node in graph[n]:
        if visited[node] == 0:
            dfs(node)

# 입력
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 정렬
for i in range(1, N + 1):
    graph[i].sort(reverse=True)

# 방문 순서를 저장
visited = [0] * (N + 1)
count = 1

# DFS 호출
dfs(R)

# 결과 출력
print('\n'.join(map(str, visited[1:])))
