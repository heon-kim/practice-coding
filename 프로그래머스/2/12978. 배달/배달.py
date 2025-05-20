from queue import PriorityQueue

def dijk(N, road, start):
    INF = int(1e9)
    dists = [INF] * (N+1)
    nexts = [[] for i in range(N+1)]
    
    for a, b, c in road:
        nexts[a].append([b, c]) #[node, dist]
        nexts[b].append([a, c])
    
    pq = PriorityQueue()
    
    dists[start]=0
    pq.put([0,start]) #[dist, node]
    
    while not pq.empty():
        cur_dist, cur_node = pq.get()
        for next_node, next_dist in nexts[cur_node]:
            temp = cur_dist + next_dist
            if temp < dists[next_node]:
                dists[next_node] = temp
                pq.put([temp, next_node])
    
    return dists
    
def solution(N, road, K):
    dists = dijk(N, road, 1)
    return sum(1 for d in dists[1:] if d <= K)

    