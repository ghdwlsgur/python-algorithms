
def solution(park, routes):
    n, m = len(park), 0
    x, y = 0, 0

    block = []
    for i in range(n):
        for j, zero in enumerate(list(park[i])):
            if zero == 'S':
                x, y = i, j
                m = len(list(park[i]))
            elif zero == 'X':
                block.append((i, j))

    for d in routes:
        d = d.split()
        direction, distance = d[0], int(d[1])

        checkpoint = [(x, y)]
        for _ in range(distance):
            if direction == 'E':
                nx, ny = x, y + 1
            elif direction == 'W':
                nx, ny = x, y - 1
            elif direction == 'S':
                nx, ny = x + 1, y
            elif direction == 'N':
                nx, ny = x - 1, y

            if nx < 0 or ny < 0 or nx >= m or ny >= m:
                x, y = checkpoint[0][0], checkpoint[0][1]
                break

            if len(block) > 0:
                if (nx, ny) in block:
                    x, y = checkpoint[0][0], checkpoint[0][1]
                    break
                # for block_x, block_y in block:
                #     if nx == block_x and ny == block_y:
                #         x, y = checkpoint[0][0], checkpoint[0][1]
                #         break
            x, y = nx, ny

    return [x, y]



print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))