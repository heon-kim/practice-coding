#nCr

def jamoCntPass():
  global r, choose
  mo = ['a','e','i','o','u']
  moCnt = 0
  jaCnt = 0
  for c in choose:
    moCnt += (c in mo)
  jaCnt = r - moCnt
  return (moCnt>=1 and jaCnt>=2)

def comb(index, level):
  global r, choose, n, arr
  if(level==r):
    if(jamoCntPass()):
      for u in choose:
        print(u, end="")
      print()
    return
    print()
  for i in range(index, n):
    choose.append(arr[i])
    comb(i+1, level+1)
    choose.pop()


r, n = map(int, input().split())
arr = input().split()
arr.sort()
choose = []

comb(0, 0)

