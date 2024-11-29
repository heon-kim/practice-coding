function solution(price, money, count) {
    total = 0
    for(let i = 1; i<=count; i++){
        total += i * price
    }
    const m = total - money
    return m > 0 ? m : 0
}