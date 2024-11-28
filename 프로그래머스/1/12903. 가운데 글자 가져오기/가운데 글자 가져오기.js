function solution(s) {
    n = s.length / 2
    if(s.length % 2 ==0){
        return s.slice(n-1, n+1)
    }else{
        return s[Math.floor(n)]
    }
}