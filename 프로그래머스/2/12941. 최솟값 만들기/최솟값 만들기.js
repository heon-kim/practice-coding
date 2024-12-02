function solution(A,B){
    A.sort((a,b)=>a-b)
    B.sort((a,b)=>b-a)
    let am = A.map((x,i)=>x*B[i])
    return am.reduce((a,b)=>a+b)
}