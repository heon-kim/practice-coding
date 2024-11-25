def solution(s):
    s = s.lower()
    ps = [p for p in s if p=='p']
    ys = [y for y in s if y=='y']
    pl = len(ps)
    yl = len(ys)
    
    if(pl == yl):
        return True
    else:
        return False