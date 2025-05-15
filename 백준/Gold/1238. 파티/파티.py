from queue import PriorityQueue
import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e12)

N, M, X = map(int, input().split()) # N명 학생, X번 마을, M개 도로(단방향)

# 도로
road_go = [[] for _ in range(N+1)]
road_come = [[] for _ in range(N+1)]

for _ in range(M):
  start_node, end_node, time = map(int, input().split())
  road_go[start_node].append([end_node, time])
  road_come[end_node].append([start_node, time])
  
# 다익스트라
def dijk(road, start):
  times = [INF] * (N+1)
  pq = PriorityQueue()
  times[start] = 0
  pq.put([start, 0])
  
  while not pq.empty():
    cur_node, cur_time = pq.get()
    for next_node, next_time in road[cur_node]:
      temp_time = cur_time+next_time
      if(temp_time<times[next_node]):
        times[next_node] = temp_time
        pq.put([next_node, temp_time])
  return times

# N개 마을
ans = -1

road_go_times = dijk(road_go, X)
road_come_times = dijk(road_come, X)

for i in range(1, N+1):
  ans = max(ans, road_go_times[i]+road_come_times[i])

print(ans)
    

