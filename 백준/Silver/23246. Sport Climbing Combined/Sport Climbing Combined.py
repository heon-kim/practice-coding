# 곱, 합, 등
# 등 b
# 점수 p,q,r
n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]
lst = []

for i in arr:
  lst.append([i[1]*i[2]*i[3], i[1]+i[2]+i[3], i[0]])

for j in sorted(lst)[:3]:
  print(j[2], end=" ")