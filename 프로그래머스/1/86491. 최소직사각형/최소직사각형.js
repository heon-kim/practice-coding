function solution(sizes) {
    const sorted = sizes.map((i)=>i.sort((a,b)=>b-a))
    const w = sorted.map((i)=>i[0])
    const h = sorted.map((i)=>i[1])
    return Math.max(...w) * Math.max(...h)
}