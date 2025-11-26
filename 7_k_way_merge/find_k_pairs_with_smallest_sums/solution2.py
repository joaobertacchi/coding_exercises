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

def k_smallest_pairs(list1, list2, k):
    heap = []
    result = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            heappush(heap, Pair(list1[i], list2[j]))
    
    for n in range(min(k, len(heap))):
        pair = heappop(heap)
        result.append([pair.u, pair.v])

    return result
