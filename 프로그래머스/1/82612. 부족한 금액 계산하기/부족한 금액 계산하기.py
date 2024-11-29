def solution(price, money, count):
    total = sum((i+1)*price for i in range(count))
    m = total - money
    return m if m > 0 else 0