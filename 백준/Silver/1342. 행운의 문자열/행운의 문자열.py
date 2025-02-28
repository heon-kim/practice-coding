# 브루트포스로 풀기

# 팩토리얼
# def fact(x):
# 	if x == 0:
# 		return 1
# 	return fact(x - 1) * x

# 인접한 문자가 없는지 확인
def isOk(n, choose):
  ok = True
  for i in range(n-1):
    if choose[i] == choose[i+1]:
      ok = False
      break
  return ok

# str의 모든 순열
def perm(index):
  global n, choose, check, ans
  if(index==n):
    if isOk(n, choose) == True:
      ans.add("".join(choose))
      # ans += 1
    return

  prev = None
  for i in range(n):
    if check[i]==True or prev == str[i]:
      continue
    choose.append(str[i])
    check[i] = True
    perm(index+1)
    choose.pop()
    check[i] = False
    prev = str[i]
    
str = sorted(input())
n = len(str)
choose = []
check = [False]*n
ans = set()
# ans = 0

perm(0)

# 중복값 제거
# for i in range(ord('a'), ord('z') + 1):
# 	ans //= fact(str.count(chr(i)))

print(len(ans))
# print(ans)


