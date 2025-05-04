T = int(input()) # 문자열의 개수

def is_hoi(str):
  left = 0
  right = len(str) - 1
  
  while right >= left:
    if str[left] != str[right]:
      return False
    left += 1
    right -= 1
  return True

def solve(str):
  left = 0
  right = len(str) - 1
  
  while right >= left:
    if str[left] != str[right]:
      s1 = str[:left]+str[left+1:]
      s2 = str[:right]+str[right+1:]
      if is_hoi(s1) or is_hoi(s2):
        return 1
      else:
        return 2  
    left += 1
    right -= 1
  return 0

for _ in range(T):
  str = input()
  print(solve(str))