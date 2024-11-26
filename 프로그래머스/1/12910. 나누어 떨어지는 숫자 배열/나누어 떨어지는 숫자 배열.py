def solution(arr, divisor):
    if(divisor == 1):
        return sorted(arr)
    return sorted([i for i in arr if i%divisor==0]) or [-1]