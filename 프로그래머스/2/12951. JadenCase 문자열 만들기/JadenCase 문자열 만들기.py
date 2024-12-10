def solution(s):
    l = s.lower()
    a =[]
    for str in l.split(" "):
        if(len(str)>1):
            a.append(str[0].upper()+str[1:])
        else:
            a.append(str.upper())
    return " ".join(a)
