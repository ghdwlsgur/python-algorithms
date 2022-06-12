def dothis():
    n = int(input())
    q = []
    if n < 100:
        for i in range(1, n+1):
            q.append(i)
    else:
        for i in range(1, 100):
            q.append(i)
        for i in range(100, n + 1):
            if (i // 100) - ((i % 100)//10) == ((i % 100)//10) - ((i % 100) % 10):
                q.append(i)
    print(len(q))


dothis()
