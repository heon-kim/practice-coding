import math

def solution(n):
    number = math.sqrt(n)
    if(math.floor(number)==math.ceil(number)):
        return (number+1)**2
    else:
        return -1