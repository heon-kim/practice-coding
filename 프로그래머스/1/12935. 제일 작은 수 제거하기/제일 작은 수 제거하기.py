import math

def solution(arr):
    if len(arr) <= 1: return [-1]
    min_ = min(arr)
    return [i for i in arr if i != min_]
