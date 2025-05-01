N = int(input()) # 지방의 수 (3<=N<=10000)
arr = sorted(map(int, input().split())) # 예산 요청
M = int(input()) # 총 예산 (N<=M<=1000,000,000)

def is_possible(maximum):
  total = 0
  for i in arr:
    if i > maximum:
      total += maximum
    else:
      total += i
  return total <= M
  
def solve():
  cur = -1
  step = int(1e9)
  while step != 0:
    while cur + step <= int(1e9) and is_possible(cur+step):
      cur += step
    step //= 2
  return cur

if sum(arr) <= M:
  print(max(arr))
else:
  print(solve())
