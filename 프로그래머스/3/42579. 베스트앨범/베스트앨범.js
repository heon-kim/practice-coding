function solution(genres, plays) {
    const genreMap = {}
    const result = []
    
    genres.forEach((genre, index)=>{
        const totalPlays = plays[index]
        if(!genreMap[genre]){
            genreMap[genre]={
                totalPlays:0,
                songs:[]
            }
        }
        genreMap[genre].totalPlays += totalPlays
        genreMap[genre].songs.push({index, totalPlays})
    })
    
    const sorted = Object.values(genreMap).sort((a,b)=>b.totalPlays - a.totalPlays)
    
    sorted.map((v)=>{
       const temp = v.songs.sort((a,b)=>b.totalPlays-a.totalPlays).slice(0,2).map(i=>i.index)
       result.push(...temp)
    }) 
    
    return result
}