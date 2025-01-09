function solution(nums) {
    const s = new Set(nums)
    const l = nums.length/2
    if(s.size <= l){
        return s.size
    }
    return l
}