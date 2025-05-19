def combinations(arr, R):
    result = []
    choose = []
    
    def comb(index, level):
        if level == R:
            return result.append(choose[:])
        for i in range(index, len(arr)):
            choose.append(arr[i])
            comb(i+1, level+1)
            choose.pop()
    
    comb(0, 0)
    return result

def solution(number):
    cnt = 0
    for a, b, c in combinations(number, 3):
        if a + b + c == 0:
            cnt += 1
    return cnt