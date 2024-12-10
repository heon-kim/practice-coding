function solution(s) {
    const l = s.toLowerCase()
    let a = []
    for(str of l.split(" ")){
        len = str.length
        if(len >1){
            a.push(str[0].toUpperCase()+str.slice(1,len))
        }else{
            a.push(str.toUpperCase())
        }
    }
    return a.join(" ")
}