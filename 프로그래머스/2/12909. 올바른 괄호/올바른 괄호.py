def solution(s):
    arr = []
    for i in list(s):
        if(i=="("):
            arr.append(i)
        else:
            if(len(arr)>0 and arr[len(arr)-1]=="("):
                arr.pop()
            else:
                arr.append(i)
    return len(arr)==0
    