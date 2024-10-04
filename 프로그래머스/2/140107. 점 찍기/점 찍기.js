function solution(k, d) {  
    if(k > d) return 1;
    if(k == d) return 3;
    let count = 0;
    const maxA = Math.floor(d / k);

    for (let a = 0; a <= maxA; a++) {
        const maxB = Math.floor(Math.sqrt(d ** 2 - (a * k) ** 2) / k);
        count += maxB + 1;
    }
    return count;
}