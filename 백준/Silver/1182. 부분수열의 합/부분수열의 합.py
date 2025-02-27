def comb(r, index, level, choose):
    global ans
    if level == r:
        if sum(choose) == S:
            ans += 1
        return
    
    for i in range(index, N):
        choose.append(arr[i])
        comb(r, i + 1, level + 1, choose)
        choose.pop()

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    comb(i, 0, 0, [])

print(ans)
