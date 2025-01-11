function solution(numbers) {
    const numberSet = new Set();
    let result = 0;

    // 1. 숫자 조합(재귀)
    combination("", numbers);

    // 2. 소수 판별
    for (let value of numberSet) {
        if (isPrime(value)) {
            result += 1;
        }
    }

    function combination(comb, others) {
        // 조합된 숫자 추가
        if (comb !== "") {
            numberSet.add(parseInt(comb, 10));
        }

        // 다른 숫자 조합 생성
        for (let i = 0; i < others.length; i++) {
            combination(comb + others[i], others.slice(0, i) + others.slice(i + 1));
        }
    }

    function isPrime(number) {
        if (number < 2) return false;
        const limit = Math.floor(Math.sqrt(number)) + 1;
        for (let i = 2; i < limit; i++) {
            if (number % i === 0) {
                return false;
            }
        }
        return true;
    }

    return result;
}
