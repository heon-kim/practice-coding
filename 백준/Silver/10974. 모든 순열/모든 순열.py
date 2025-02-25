import sys

def perm(level):
  global N, choose, check
  
  if(level==N):
    print(" ".join(map(str,choose)))
    return
    
  for i in range(1, N+1):
    if check[i]==True:
      continue
      
    choose.append(i)
    check[i]=True
    
    perm(level+1)
    
    choose.pop()
    check[i]=False


N = int(input())
choose = []
check=[False]*(N+1)

perm(0)