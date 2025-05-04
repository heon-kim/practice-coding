N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0
total = 0
count = 0

while True:
    if total >= M:
        total -= A[start]
        start += 1
    elif end == N:
        break
    else:
        total += A[end]
        end += 1

    if total == M:
        count += 1

print(count)