def solution(a, b):
    if(a==b):
        return a
    if(a>b):
        max_=a
        min_=b
    else:
        max_=b
        min_=a
    return sum([i for i in range(min_, max_ + 1)])