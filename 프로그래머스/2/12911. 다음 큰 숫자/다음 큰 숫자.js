function countOnes(bin){
    return [...bin].filter(i=>i==1).length
}

function solution(n) {
    const firstOnes = countOnes(n.toString(2))
    
   while(true){
       n += 1
       if(firstOnes==countOnes(n.toString(2))){
           return n
       }
   }
}