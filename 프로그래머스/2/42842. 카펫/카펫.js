function solution(brown, yellow) {
    // x*y=>brown+yellow
    // (x-2)*(y-2)=>yellow
    let xPlusY = Math.floor((brown+4)/2)
    
    for(let x = 3; x<=xPlusY-3; x++){
        const y = xPlusY-x
        if(x>=y && x*y==brown+yellow){
            return [x,y]
        }
    }
    
}