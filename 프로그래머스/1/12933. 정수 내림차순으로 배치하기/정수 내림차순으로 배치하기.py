def solution(n):
    answer = 0
    li = sorted(list(str(n)))
    for i in range(len(li)):
        answer += int(li[i]) * (10**i)
    return answer
    