import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

heapq.heappop(heap)
heapq.heappop(heap)

print(heap)
