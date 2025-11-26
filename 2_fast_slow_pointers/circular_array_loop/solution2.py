def visit(index, c_visited, visited, dir, nums, last_visited):
    print("visiting %d" % index)
    if dir[0] == None:
        dir[0] = nums[index]
    elif (dir[0]*nums[index] < 0):
        c_visited.clear()
        dir[0] = None
        print("Output: next")
        return "next"

    if index in c_visited and index != last_visited[0]:
        print("Output: cycle")
        print(c_visited)
        return "cycle"
    if index in visited:
        print("Output: next")
        c_visited.clear()
        dir[0] = None
        return "next"
    c_visited.add(index)
    visited.add(index)
    print("Output: continue")
    last_visited[0] = index
    return "continue"

def circular_array_loop(nums):
    visited = set()
    c_visited = set()
    dir = [None]
    last_visited = [None]
    
    index = 0
    next_index = index
    
    while True:
        decision = visit(next_index, c_visited, visited, dir, nums, last_visited)
        if decision == "cycle":
            return True
        elif decision == "continue":
            next_index = (next_index + nums[next_index]) % len(nums)
        elif decision == "next":
            index += 1
            while index in visited and index < len(nums):
                index += 1
            if index >= len(nums):
                return False
            next_index = index

    return False
