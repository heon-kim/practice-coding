def solution(arr):
    a2 = []
    for i in arr:
        if(len(a2)==0 or a2[-1]!=i):
            a2.append(i)
    return a2
        