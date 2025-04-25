import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 늘리기

T = int(sys.stdin.readline())
 
xp = [0, 0, 1, -1]
yp = [1, -1, 0, 0]

def dfs(x, y):
  visited[y][x]=True
  for i in range(4):   
    nx=x+xp[i]
    ny=y+yp[i]
    if(0<=nx<M and 0<=ny<N):
      if not visited[ny][nx] and arr[ny][nx]==1:
          dfs(nx, ny)

for _ in range(T):  
  M, N, K = map(int, sys.stdin.readline().split())
  visited = [[False]*M for _ in range(N)]
  arr = [[0]*(M) for _ in range(N)]
  
  for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    arr[y][x]=1
  
  count = 0
  for i in range(N):
    for j in range(M):
      if not visited[i][j] and arr[i][j]==1:
        count += 1
        dfs(j,i)
  
  print(count)