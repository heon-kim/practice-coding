function solution(n) {
    let str = ""
    const repeat = Math.floor(n / 2)
    for(let i = 0; i< repeat ; i++){
        str += "수박"
    }
    if(n%2 == 1){
        str += "수"
    }
    return str
}