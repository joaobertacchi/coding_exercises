def next(pos, nums):
    return (pos + nums[pos]) % len(nums)
def can_move(pos, is_forward, nums):
    next_pos = next(pos, nums)
    if pos == next_pos:
        return False
    if nums[next_pos] > 0:
        return is_forward
    return not is_forward
    
def circular_array_loop(nums):
    slow_visited = [False]*len(nums)
    for i in range(len(nums)):
        if slow_visited[i]:
            continue
            
        fast = slow = i
        slow_visited[slow] = True
        is_forward = nums[i] > 0
        count = 0
        while can_move(slow, is_forward, nums) and can_move(fast, is_forward, nums) and can_move(next(fast, nums), is_forward, nums) and count < len(nums):
            count += 1
            slow = next(slow, nums)
            fast = next(next(fast, nums), nums)
            if slow == fast:
                return True
            if slow_visited[slow]:
                break
            slow_visited[slow] = True
    return False
