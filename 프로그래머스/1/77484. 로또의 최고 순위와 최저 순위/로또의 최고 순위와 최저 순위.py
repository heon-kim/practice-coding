def solution(lottos, win_nums):
    zero_cnt = 0
    win_cnt = 0
    
    for i in lottos:
        if i == 0:
            zero_cnt += 1
    
    for i in lottos:
        if i in win_nums:
            win_cnt += 1
    
    max_rank = 7 - (zero_cnt+win_cnt) if zero_cnt+win_cnt >= 1 else 6
    min_rank = 7 - win_cnt if win_cnt >= 1 else 6
    
    return [max_rank, min_rank]