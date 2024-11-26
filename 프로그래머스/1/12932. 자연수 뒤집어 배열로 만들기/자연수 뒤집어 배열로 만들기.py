def solution(n):
    arr = []
    while n>0:
        arr.append(n%10)
        n=n//10
    return arr
        