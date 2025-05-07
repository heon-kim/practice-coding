function numberOneCnt(bin){
    let cnt = 0 
    for (i of bin){
        if(i=='1'){
            cnt += 1
        }
    }
    return cnt
}

function solution(n) {
    const firstBinary = n.toString(2)
    
   while(true){
       n += 1
       if(numberOneCnt(firstBinary)==numberOneCnt(n.toString(2))){
           break
       }
   }
    
   return n
}