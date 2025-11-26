from heapq import *

def kth_smallest_element(matrix, k):
    n = len(matrix)
    heap = []
    e_count = 0
    num = None

    i = j = 0
    while i < n:
        heappush(heap, (matrix[i][j], i, j))
        i += 1
        
    while e_count != k:
        num, i, j = heappop(heap)
        e_count += 1
        if j + 1 < n:
            heappush(heap, (matrix[i][j+1], i, j + 1))
    return num
