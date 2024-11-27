def solution(numbers):
    set1 = set([i for i in range(10)])
    set2 = set(numbers)
    return sum(list(set1 - set2))