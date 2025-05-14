from queue import PriorityQueue

INF = int(1e9)
MAX = int(1e5)

N, K = map(int, input().split())

time = [INF]*(MAX+1)
pq = PriorityQueue()

time[N] = 0
pq.put([0, N]) # [time, node]

while not pq.empty():
  current_time, current_node = pq.get()

  nexts = [
    [current_time+1, current_node-1],
    [current_time+1, current_node+1],
    [current_time, current_node*2]
  ]

  for next_time, next_node in nexts:
    if(0<=next_node<=MAX):
      if(next_time<time[next_node]):
        time[next_node]=next_time
        pq.put([next_time, next_node])

print(time[K])