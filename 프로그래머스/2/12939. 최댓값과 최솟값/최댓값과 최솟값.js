function solution(s) {
    list = s.split(" ").map(i=>parseInt(i))
    list.sort((x,y)=>{
        if(x>y) return 1
        return -1
    })
    return list[0]+" "+list[list.length-1]
}