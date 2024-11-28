function solution(s){
    let arrS = s.split("")
    let ar = []
    for(a of arrS){
        if(a=="("){
            ar.push(a)
        }else if(a==")"){
            if(ar[ar.length-1]=="("){ ar.pop(a) }
            else{ ar.push(a) }
        }
    }
    if(ar.length>0){
        return false
    }
    return true
}
