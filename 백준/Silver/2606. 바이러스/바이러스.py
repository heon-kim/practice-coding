def dfs(cur):
	global visited, answer, graph
	visited[cur] = True
	answer += 1
 
	for next in range(1, N+1):
		if(not visited[next] and graph[cur][next]):
			dfs(next)
 
N = int(input())
M = int(input())
 
# 그래프
graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
answer=0
 
for _ in range(M):
	x,y=map(int, input().split())
	graph[x][y]=True
	graph[y][x]=True
 
# dfs
dfs(1)
 
# 출력
print(answer-1)