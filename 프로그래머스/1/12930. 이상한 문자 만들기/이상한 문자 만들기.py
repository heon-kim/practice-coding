def solution(s):
    arr=[]
    for x in s.split(" "):
        str=""
        for y in range(len(x)):
            if(y%2==0):
                str += x[y].upper()
            else:
                str += x[y].lower()
        arr.append(str)
    return " ".join(arr)