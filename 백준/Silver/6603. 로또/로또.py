def comb(idx, lev):
  global choose, arr, k
  
  if lev==6:
    for u in choose:
      print(u, end=" ")
    print()
    return

  for i in range(idx, k):
    choose.append(arr[i])
    comb(i+1, lev+1)
    choose.pop()

while True:
  choose = []
  ipt = list(map(int, input().split()))
  k = ipt[0]
  arr = ipt[1:]
  if k == 0:
    break
  comb(0,0)
  print()