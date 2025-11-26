from functools import cmp_to_key

def comparator(a, b):
    if a[0] < b[0]:
        return -1
    if a[0] == b[0]:
        if a[1] == 'e':
            return -1
        else:
            return 1
    if a[0] > b[0]:
        return 1

def find_sets(intervals):
    times = []
    for i in intervals:
        times.append([i[0], 's'])
        times.append([i[1], 'e'])
    times.sort(key=cmp_to_key(comparator))
    
    count = 0
    rooms = 0
    for t in times:
        if t[1] == 'e':
            count -= 1
        else:
            count += 1
        rooms = max(rooms, count)

    return rooms