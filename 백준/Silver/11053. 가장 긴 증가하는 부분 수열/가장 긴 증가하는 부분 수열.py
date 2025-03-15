N = int(input())
arr = [0]+list(map(int, input().split()))

dp = [-1]*(N+1)

dp[1] = 1

for i in range(1, N+1):
  best = 0
  for j in range(1, N):
    if arr[i] > arr[j]:
      best = max(best, dp[j])
  dp[i] = best + 1

print(max(dp))