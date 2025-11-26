def window_size(start, end):
    return end - start + 1

def longest_repeating_character_replacement(s, k):
    count = {}
    max_freq = 0
    max_window_size = 0
    start = 0
    
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        max_freq = max(count[s[end]], max_freq)
        
        while window_size(start, end) - max_freq > k:
            count[s[start]] -= 1
            start += 1
        max_window_size = max(max_window_size, window_size(start, end))
    
    return max_window_size
