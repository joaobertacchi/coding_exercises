from functools import cmp_to_key

def merge_intervals(intervals):

    def comparator(a, b):
        if a[0] <  b[0]:
            return -1
        elif a[0] ==  b[0]:
            return 0
        else:
            return 1
    def merge(a, b):
        if b[0] > a[1]:
            return [a, b]
        if b[1] <= a[1]:
            return [a]
        if b[0] <= a[1]:
            return [[a[0], b[1]]]
        
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=cmp_to_key(comparator))
    output = merge(intervals[0], intervals[1])
    i = 2
    while i < len(intervals):
        a = output.pop()
        b = intervals[i]
        output = output + merge(a,b)
        i += 1
        
    return output
