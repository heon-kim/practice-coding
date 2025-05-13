import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue

INF = int(1e12)

N, E = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  adj_list[a].append([b,c]) # node, dist
  adj_list[b].append([a,c])

def dijks(start):
  dist = [INF] * (N+1)
  pq = PriorityQueue()

  dist[start] = 0
  pq.put([start, 0])

 
  while not pq.empty():
    cur_node, cur_dist = pq.get()
    for adj_node, adj_dist in adj_list[cur_node]:
      temp_dist = cur_dist + adj_dist
      if(temp_dist<dist[adj_node]):
        dist[adj_node] = temp_dist
        pq.put([adj_node, temp_dist])
      
  return dist

v1, v2 = map(int, input().split())
dist_1 = dijks(1)
dist_v1 = dijks(v1)
dist_v2 = dijks(v2)

res1 = dist_1[v1]+dist_v1[v2]+dist_v2[N]
res2 = dist_1[v2]+dist_v2[v1]+dist_v1[N]
ans = min(res1, res2)

print(ans if ans < INF else -1)