function solution(s) {
    list = s.split(" ")
    return Math.min(...list)+" "+Math.max(...list)
}