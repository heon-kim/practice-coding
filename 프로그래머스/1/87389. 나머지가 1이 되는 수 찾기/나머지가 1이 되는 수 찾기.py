def solution(n):
    x = 1
    while n % x != 1: 
        x = x + 1
    return x
        