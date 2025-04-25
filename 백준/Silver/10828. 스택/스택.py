import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().strip().split()
    
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        print(-1 if not stack else stack.pop())
    elif cmd[0] == 'top':
        print(-1 if not stack else stack[-1])
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if not stack else 0)
