function solution(number, k) {
    const stack = [];

    for (digit of number){
        
        while(k>0 && stack.length>0 && stack[stack.length-1] < digit){
            stack.pop()
            k -= 1
        }
        
        stack.push(digit)
    }
    
    return stack.slice(0, number.length - k).join("")
}
