# 1. 브루트포스로 풀수 있는가?
# n^2칸을 상하좌우 방향으로 확인: 4n^2
# 연속한 칸의 개수 확인(열, 행): 2n^2
# 총 8n^4 (n<=50): 약 60,000,000

def get_best():
  global N, board
  best = 0

  for i in range(N):
    bef = '-'
    value = 0
    for j in range(N):
      if bef != board[i][j]:
        value = 1
      else:
        value += 1
      bef = board[i][j]
      best = max(best, value)

  for j in range(N):
    bef = '-'
    value = 0
    for i in range(N):
      if bef != board[i][j]:
        value = 1
      else:
        value += 1
      bef = board[i][j]
      best = max(best, value)
  return best

# 입력 받기
N = int(input())
board = [list(input()) for _ in range(N)]
ans = 0

# 보드 한 칸의 상하좌우를 확인
dy = [-1, 1, 0, 0] # 상, 하, 좌, 우
dx = [0, 0, -1, 1] # 상, 하, 좌, 우

for cx in range(N):
  for cy in range(N):
    for i in range(4):
      nx = cx+dx[i]
      ny = cy+dy[i]
      if (nx < N) and (ny < N):
        if board[cx][cy] != board[nx][ny]:
          board[cx][cy], board[nx][ny] = board[nx][ny], board[cx][cy]
          ans = max(ans, get_best())
          board[cx][cy], board[nx][ny] = board[nx][ny], board[cx][cy]

print(ans)
          