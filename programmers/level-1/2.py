
def solution(name, yearning, photo):

    answer = []
    name_with_yearning = { n : 0 for n in name }
    for i in range(len(yearning)):
        name_with_yearning[name[i]] = yearning[i]

    tot = 0
    for name_list in photo:
        for n in name_list:
            if n in name:
                tot += name_with_yearning[n]
        answer.append(tot)
        tot = 0

    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))