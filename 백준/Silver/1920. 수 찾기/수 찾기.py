import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) # 이 수들이 A안에 존재하는지 알아내기  

def func(num):
  left = 0
  right = len(A)-1

  while left <= right:
    mid = (left+right)//2
    if A[mid] < num:
      left = mid + 1
    elif A[mid] > num:
      right = mid - 1
    elif A[mid] == num:
      return 1
      
  return 0

for num in arr:
  print(func(num))


# 오답노트
# num in A => 시간초과!!
# sort 후 이진탐색 => 시간초과!!