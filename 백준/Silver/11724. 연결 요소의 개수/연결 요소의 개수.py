N, M = map(int, input().split())

visited = [False]*(N+1)
arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
  u, v = map(int, input().split())
  arr[u][v]=1
  arr[v][u]=1

def dfs(start):
  visited[start]=True
  for i in range(1, N+1):
    if not visited[i] and arr[start][i]==1:
      dfs(i)

count = 0
for i in range(1, N+1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)