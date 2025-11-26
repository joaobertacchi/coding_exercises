def is_nucleotide(c):
    return c in ['A','C', 'G', 'T']

def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []
    sequence_count = {}
    start = 0
    end = 9
    
    count = 0
    for i in range(start, end+1):
        if is_nucleotide(s[i]):
            count += 1
    
    
    if count == 10:
        sequence_count[s[start:end+1]] = sequence_count.get(s[start:end+1], 0) + 1
    while end < len(s) - 1:
        if is_nucleotide(s[start]):
            count -= 1
        start += 1
        end += 1
        if is_nucleotide(s[end]):
            count += 1
        
        if count == 10:
            sequence_count[s[start:end+1]] = sequence_count.get(s[start:end+1], 0) + 1
        
    l = []
    
    for key, value in sequence_count.items():
        if value > 1:
            l.append(key)
    return l
