def solution(nums):
    l = len(nums) / 2
    s = set(nums)
    if len(s) <= l:
        return len(s)
    return l