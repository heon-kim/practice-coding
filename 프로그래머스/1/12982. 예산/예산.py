def solution(d, budget):
    s = sorted(d)
    count = 0
    for i in s:
        if(budget-i>=0):
            budget = budget - i
            count += 1
    return count