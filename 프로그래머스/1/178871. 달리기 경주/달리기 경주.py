def solution(players, callings):
    rank = {}
    
    for i in range(len(players)):
        rank[players[i]] = i
    
    for name in callings:
        idx = rank[name]
        prev_name = players[idx - 1]

        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        rank[name] -= 1
        rank[prev_name] += 1

    return players