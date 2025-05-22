# 투포인터

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
cnt = 0 
current = 0

while True:
  if current >= M:
    current -= arr[left]
    left += 1
  elif right >= N:
    break
  else:
    current += arr[right]
    right += 1

  if current == M:
    cnt += 1

print(cnt)