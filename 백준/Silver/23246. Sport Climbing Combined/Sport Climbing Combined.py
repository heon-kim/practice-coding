n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]

def comp(x):
  return [x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]]

lst = sorted(arr, key=comp)

for b,p,q,r in lst[:3]:
  print(b, end=" ")