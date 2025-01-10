function solution(answers) {
    const scores = [
        {id:1, answer:[1, 2, 3, 4, 5], score:0},
        {id:2, answer:[2, 1, 2, 3, 2, 4, 2, 5], score:0},
        {id:3, answer:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5], score:0},
    ]
    
    for(let i = 0; i<answers.length; i++){
        if(answers[i]==scores[0].answer[i%5]) scores[0].score += 1
        if(answers[i]==scores[1].answer[i%8]) scores[1].score += 1
        if(answers[i]==scores[2].answer[i%10]) scores[2].score += 1
    }
    
    const winners = scores.filter((item)=>item.score == Math.max(...scores.map(i=>i.score)))
    
    return winners.map(item=>item.id).sort((a,b)=>a-b)
}