N = int(input())
arr = [0]+list(map(int, input().split()))

dp = [0]*(N+1)

for n in range(N+1):
  dp[n]=max(0, dp[n-1])+arr[n]


print(max(dp[1:]))