def solution(arr, divisor):
    arr.sort()
    if(divisor == 1):
        return arr
    arr2 = [i for i in arr if i%divisor==0]
    if(len(arr2)<=0):
        return [-1]
    return arr2