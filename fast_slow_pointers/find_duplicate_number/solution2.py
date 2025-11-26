def find_duplicate(nums):
    numbers = set()
    for value in nums:
        prev_size = len(numbers)
        numbers.add(value)
        after_size = len(numbers)
        if prev_size == after_size:
            return value
    
    return 0
