N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]

for x, y in sorted(arr):
  print(x, y)