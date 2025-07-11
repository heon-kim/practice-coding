import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

min_num = 1_000_000_000
max_num = -1_000_000_000

def dfs(index, current_value, plus, minus, multiply, divide):
    global min_num, max_num

    if index == N:
        min_num = min(min_num, current_value)
        max_num = max(max_num, current_value)
        return

    if plus:
        dfs(index + 1, current_value + A[index], plus - 1, minus, multiply, divide)
    if minus:
        dfs(index + 1, current_value - A[index], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(index + 1, current_value * A[index], plus, minus, multiply - 1, divide)
    if divide:
        next_value = int(current_value / A[index]) if current_value >= 0 else -int(abs(current_value) / A[index])
        dfs(index + 1, next_value, plus, minus, multiply, divide - 1)

dfs(1, A[0], plus, minus, multiply, divide)
print(max_num)
print(min_num)
