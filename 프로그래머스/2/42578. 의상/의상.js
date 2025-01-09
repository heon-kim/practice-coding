function solution(clothes) {
    var answer = 1;
    let m = new Map();
    
    for(let [name, kind] of clothes) {
        if(m.has(kind)) m.set(kind, m.get(kind) + 1);
        else m.set(kind, 1);
    }
    
    for(let i of m.values()) {
        answer *= (i+1)
    }
    
    answer -= 1;
    return answer;
}