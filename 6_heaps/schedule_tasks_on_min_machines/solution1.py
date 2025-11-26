from functools import cmp_to_key
import heapq

def comparator(a, b):
    if a[0] < b[0]:
        return -1
    if b[0] < a[0]:
        return 1
    if a[1] < b[1]:
        return -1
    if a[1] > b[1]:
        return 1
    return 0

def minimum_machines(tasks):
    tasks.sort(key=cmp_to_key(comparator))
    heap = []
    max_size = 0
    for task in tasks:
        task_start, task_end = task
        while len(heap) != 0 and task_start >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, task_end)
        max_size = max(len(heap), max_size)
    return max_size
