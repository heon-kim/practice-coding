function solution(nums) {
    const s = new Set(nums)
    const l = nums.length/2
    return Math.min(s.size, l)
}