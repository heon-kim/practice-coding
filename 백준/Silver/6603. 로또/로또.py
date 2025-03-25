def comb(index, level):
  global n, r, arr, choose

  if(level==r):
    for u in choose:
      print(u, end=" ")
    print()
    return 
  for i in range(index, n):
    choose.append(arr[i])
    comb(i+1, level+1)
    choose.pop()

while True:
  I = list(map(int, input().split()))
  n = I[0]
  r = 6
  arr = I[1:]
  choose = []

  if(n==0):
    break

  comb(0, 0)
  print()