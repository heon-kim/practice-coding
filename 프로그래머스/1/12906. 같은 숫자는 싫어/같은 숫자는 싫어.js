function solution(arr){
    let a2 = []
    for (i of arr){
        if(!a2 || a2[a2.length-1]!=i){
            a2.push(i)
        }
    }
    return a2
}