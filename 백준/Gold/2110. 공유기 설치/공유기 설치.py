import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

def is_possible(distance):
  count = 1
  last_house_index = 0
  
  for i in range(1, N):
    if(houses[i] - houses[last_house_index] >= distance):
      count += 1
      last_house_index = i
  return count >= C

distance = -1
step = int(1e9) + 1

while step!=0:
  while distance+step<=int(1e9) and is_possible(distance+step):
    distance += step
  step //= 2

print(distance)