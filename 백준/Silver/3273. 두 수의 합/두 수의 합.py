# 투포인터

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

left = 0
right = len(a) - 1
cnt = 0

while (left < right):
  cur = a[left]+a[right]
  if cur == x:
    cnt += 1
    left += 1
  elif cur < x:
    left += 1
  else:
    right -= 1

print(cnt)