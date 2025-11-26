import heapq

def k_smallest_number(lists, k):
    total_size = 0
    max_elem = None
    min_heap = []
    removed_count = 0
    last = None
    
    for i in range(len(lists)):
        list = lists[i]
        if len(list) == 0:
            continue
        total_size += len(list)
        if max_elem == None:
            max_elem = list[-1]
        else:
            max_elem = max(max_elem, list[-1])
        heapq.heappush(min_heap, (list[0], i, 0))
        
    if total_size == 0:
        return 0
    if k > total_size:
        return max_elem

    while removed_count < k and len(min_heap) > 0:
        elem, list_index, elem_index = heapq.heappop(min_heap)
        last = elem
        removed_count += 1
        next_elem_index = elem_index + 1
        if next_elem_index < len(lists[list_index]):
            heapq.heappush(min_heap, (lists[list_index][next_elem_index], list_index, next_elem_index))
    
    return last
