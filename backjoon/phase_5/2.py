def dothis():
    q = []
    not_q = []

    for i in range(0, 100):
        d = i + (i // 10) + (i % 10)
        q.append(d)
    for i in range(100, 1000):
        d = i + (i // 100) + ((i % 100)//10) + ((i % 100) % 10)
        q.append(d)
    for i in range(1000, 10000):
        d = i + (i // 1000) + ((i % 1000)//100) + \
            (((i % 1000) % 100)//10) + (((i % 1000) % 100) % 10)
        q.append(d)
    for j in range(0, 10000):
        if j not in q:
            not_q.append(j)
    not_q.sort()
    for res in not_q:
        print(res)


dothis()
