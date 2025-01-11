import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
   global visited, graph
   visited[idx] = 1
   for i in range(1, N+1):
      if not visited[i] and graph[idx][i]:
         dfs(i)

# MAX = 1000+2
N, M = map(int, input().split())
graph = [[0]*(N+1)for _ in range(N+1)]
visited = [0]*(N+1)
answer=0

#1. graph에 연결 정보 채우기
for _ in range(M):
   u, v = map(int, input().split())
   graph[u][v] = 1
   graph[v][u] = 1

#2. DFS 호출
for i in range(1,N+1):
   if not visited[i]:
      dfs(i)
      answer += 1

#3. 출력
print(answer)