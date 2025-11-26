import heapq

def connect_sticks(sticks):
    if len(sticks) <=1:
        return 0
        
    min_heap = []
    cost = 0
    for stick in sticks:
        heapq.heappush(min_heap, stick)
    while len(min_heap) > 1:
        min_stick1 = heapq.heappop(min_heap)
        min_stick2 = heapq.heappop(min_heap)
        new_stick = min_stick1 + min_stick2
        cost = new_stick + cost
        heapq.heappush(min_heap, new_stick)
    return cost
