def solution(t, p):
    l = len(p)
    count = 0
    for i in range(len(t)-len(p)+1):
        if(int(t[i:i+l])<=int(p)):
            count+=1
    return count