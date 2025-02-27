# 브루트 포스로 풀어보기

# 1. 9P3 경우의수 모두 찾기
choose=[]
check=[False]*(10)
perms = []

def perm(index):
  if(index==3):
    perms.append(choose[:])
    return
  for i in range(1,10):
    if not check[i]:
      choose.append(i)
      check[i]=True
      perm(index+1)
      choose.pop()
      check[i]=False
      
perm(0)

# 2. 9P3에서 적절한 숫자 찾기
N=int(input())
infos = [ input().split() for _ in range(N)]
ans = 0

for cur in perms:
  ok = True  # 처음에는 가능하다고 가정

  for num, st, bl in infos:
      cur_st = cur_bl = 0
  
      for i in range(3):
          if str(cur[i]) == num[i]:
              cur_st += 1
          elif str(cur[i]) in num:
              cur_bl += 1

      if cur_st != int(st) or cur_bl != int(bl):
          ok = False
          break  # 하나라도 안 맞으면 바로 중단
    
  if ok:
      ans += 1  # 모든 조건을 통과한 경우에만 증가
      
print(ans)        
  