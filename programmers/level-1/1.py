# def solution(players, callings):
#     p = {player: i for i, player in enumerate(players)}
#     for name in callings:
#         idx = p[name]
#         players[idx], players[idx-1] = players[idx-1], players[idx]
#         p[name] = idx - 1
#         p[players[idx]] = idx
#
#     return players

# def solution(players, callings):
#     p = {player: i for i, player in enumerate(players)}
#     for name in callings:
#         idx = p[name]
#         players[idx], players[idx-1] = players[idx-1], players[idx]
#         p[name] = idx - 1
#         p[players[idx]] = idx
#     return players

# def solution(players, callings):
#     p = {player: i for i, player in enumerate(players)}
#     for name in callings:
#         idx = p[name]
#         players[idx], players[idx-1] = players[idx-1], players[idx]
#         p[name] = idx - 1
#         p[players[idx]] = idx
#     return players

def solution(players, callings):
    p = {player: i for i, player in enumerate(players)}
    for name in callings:
        idx = p[name]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        p[name] = idx - 1
        p[players[idx]] = idx
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

