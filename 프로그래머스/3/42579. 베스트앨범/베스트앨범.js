function solution(genres, plays) {
    let obj = {}
    let answer = []
    
    for(let i = 0; i < genres.length; i++){
        const g = genres[i]
        const p = plays[i]
        const ii = [i, p]
        if(obj[g]){
            obj[g].sum += p
            obj[g].arr.push(ii)
        }else{
            obj[g] ={
                sum: p,
                arr:[ii]
            } 
        }
    }
    
    const sorted = Object.values(obj).sort((a,b)=>{
       return b.sum - a.sum
    })
    
    for(let s of sorted){
        const a = s.arr
        const ss = a.sort((a,b)=>{
            return b[1]-a[1]
        })
        
        answer.push(ss[0][0])
        
        if(ss.length>=2){
            answer.push(ss[1][0])
        }
    }
    return answer
}