n=int(input())

# 피보나치 함수
def fibb(n):
  if(n==0):
    return 0
  if(n==1):
    return 1
  return fibb(n-1)+fibb(n-2)

# 실행
print(fibb(n))