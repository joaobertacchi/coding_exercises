from heapq import *

class Pair:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        
    def __gt__(self, pair):
        if self.u + self.v == pair.u + pair.v:
            return self.u > pair.u
        return self.u + self.v > pair.u + pair.v
        
    def __lt__(self, pair):
        if self.u + self.v == pair.u + pair.v:
            return self.u < pair.u
        return self.u + self.v < pair.u + pair.v
        
    def __eq__(self, pair):
        return self.u + self.v == pair.u + pair.v

def list_next(elem):
    sum, i, j = elem
    return (i, j + 1)

def k_smallest_pairs(list1, list2, k):
    result = []
    if len(list1) == 0 or len(list2) == 0:
        return result
    heap = []
    
    i = j = 0
    while i < len(list1):
        heappush(heap, (list1[i] + list2[j], i, j))
        i += 1
    
    while len(heap) > 0:
        elem = heappop(heap)
        sum, i, j = elem
        m, n = list_next(elem)
        if n < len(list2):
            heappush(heap, (list1[m]+list2[n], m, n))
        result.append([list1[i], list2[j]])
        if len(result) == k:
            return result
            
    return result
