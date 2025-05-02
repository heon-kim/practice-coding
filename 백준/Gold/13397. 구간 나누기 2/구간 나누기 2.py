N, M = map(int, input().split())
arr = list(map(int, input().split()))

def sovle(k):
  count = 1
  
  cur_min = arr[0]
  cur_max = arr[0]

  for i in range(1, N):
    cur_min = min(cur_min, arr[i])
    cur_max = max(cur_max, arr[i])

    # 현재 구간에서 최대 - 최소가 k 초과되면 구간을 나눔
    if cur_max - cur_min > k:
      cur_min = arr[i]
      cur_max = arr[i]
      count += 1
    
  return count <= M
  
cur = -1
step = max(arr)

while step!=0:
  while cur+step<=max(arr) and not sovle(cur+step):
    cur += step
  step //= 2

print(cur + 1)