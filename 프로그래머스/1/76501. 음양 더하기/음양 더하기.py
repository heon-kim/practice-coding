def solution(absolutes, signs):
    sum=0
    idx=0
    for sign in signs:
        if(sign==True):
            sum += absolutes[idx]
        else:
            sum -= absolutes[idx]
        idx += 1
    return sum
            