# 입력 받기
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 체스판 경우의 수 2개
chess1 = [[0]*8 for _ in range(8)]
chess2 = [[0]*8 for _ in range(8)]

# 체스판 채우기
for i in range(8):
  for j in range(8):
    if (i+j)%2==0:
      chess1[i][j]='B'
      chess2[i][j]='W'
    else:
      chess1[i][j]='W'
      chess2[i][j]='B'

# 최소값 찾기
def find(n,m):
  chill1 = 0
  chill2 = 0
  for i in range(8):
    for j in range(8):
      chill1 += (chess1[i][j] != board[n+i][m+j])
      chill2 += (chess2[i][j] != board[n+i][m+j])
  return min(chill1, chill2)

# 보드를 체스판만큼 자르기
minimum = int(1e12)
for n in range(N-7):
  for m in range(M-7):
    minimum = min(minimum, find(n,m))

print(minimum)