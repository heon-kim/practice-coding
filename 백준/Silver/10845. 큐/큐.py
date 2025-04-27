import sys

N = int(sys.stdin.readline())
que = []

for _ in range(N):
  cmd = sys.stdin.readline().strip()
  if 'push' in cmd:
    que.append(int(cmd.split()[1]))
  elif cmd == 'pop':
    print(-1 if not que else que[0])
    que=que[1:]
  elif cmd == 'size':
    print(len(que))
  elif cmd == 'empty':
    print(1 if not que else 0)
  elif cmd == 'front':
    print(-1 if not que else que[0])
  elif cmd == 'back':
    print(-1 if not que else que[-1])