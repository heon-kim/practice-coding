def yak(a,b):
    if(a%b==0):
        return b
    return yak(b, a%b)

def bae(a,b):
    if(a%b==0):
        return a
    return a*b
    
def solution(n, m):
    if(n>m):
        y = yak(n,m)
    else:
        y = yak(m,n)
    
    b = n*m/y
    return [y,b]