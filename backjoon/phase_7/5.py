

room = 0
for i in range(int(input())):
    H, W, N = map(int, input().split())
    if N <= H * W:
        if N % H != 0:
            room = (N % H) * 100 + (N // H) + 1
        else:
            room = H * 100 + N // H
        print(room)
