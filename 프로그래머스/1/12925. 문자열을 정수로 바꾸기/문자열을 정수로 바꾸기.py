def solution(s):
    f = s[0]
    r = s[1:]
    if(f=='-'):
        return -1 * int(r)
    elif(f=='+'):
        return int(r)
    else:
        return int(s)
    