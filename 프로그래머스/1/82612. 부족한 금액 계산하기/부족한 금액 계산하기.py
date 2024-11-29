def solution(price, money, count):
    total = 0
    for i in range(count):
        total += (i+1)*price
    m = total - money
    return m if m > 0 else 0