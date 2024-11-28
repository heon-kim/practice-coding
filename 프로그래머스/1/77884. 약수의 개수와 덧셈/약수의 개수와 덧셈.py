def pCnt(i):
    cnt=0
    for n in range(1, i+1):
        if i % n == 0:
            cnt+=1
    return cnt

def solution(left, right):
    sum = 0
    arr = [i for i in range(left, right+1)]
    for i in arr:
        if(pCnt(i) % 2 == 1):
            sum -= i
        else:
            sum += i
    return sum