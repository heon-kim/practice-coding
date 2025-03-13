N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[0,0,0]]+arr

dp = [[0,0,0] for _ in range(N+1)]

for i in range(1, N+1):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[N]))
  