def solution(strings, n):
    arr = sorted([s[n]+s for s in strings])   
    return [j[1:] for j in arr]
    
    