import sys
input = lambda: sys.stdin.readline().rstrip()

# input
N, H = map(int, input().split())

downs = [0] * (H + 1)
ups = [0] * (H + 1)

for i in range(N):
	num = int(input())
	if i % 2 == 0:
		ups[num] += 1
	else:
		downs[H - num + 1] += 1

# solve
min_num = int(1e12)
min_count = 0

obs_num = N // 2
for h in range(1, H + 1):
    obs_num -= ups[h - 1]
    obs_num += downs[h]
	
    if min_num == obs_num:
        min_count += 1

    if min_num > obs_num:
        min_num = obs_num
        min_count = 1

print(min_num, min_count)
