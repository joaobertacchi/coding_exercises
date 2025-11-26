from functools import cmp_to_key

def comparator(e1, e2):
    if e1[0] < e2[0]:
        return -1
    elif e1[0] == e2[0]:
        if e1[1] == 'end':
            return -1
        else:
            return 1
    else:
        return 1

def minimum_machines(tasks):
    events = []
    for t in tasks:
        events.append([t[0], 'start'])
        events.append([t[1], 'end'])
        
    events.sort(key=cmp_to_key(comparator))
    
    max_machines = 0
    counter = 0
    for e in events:
        if e[1] == 'start':
            counter += 1
        else:
            counter -= 1
        max_machines = max(counter, max_machines)

    return max_machines
