N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

count = 0

for i in sorted(arr, reverse=True):
  if(i<=K):
    count += K//i
    K = K%i

print(count)
  