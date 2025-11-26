def three_sum(nums):
    list.sort(nums)
    triplets = set()
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = -1*(nums[j] + nums[k])
            if sum == nums[i]:
                triplets.add((nums[i], nums[j], nums[k]))
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif sum < nums[i]:
                k -= 1
            else:
                j += 1
                
    return list(triplets)
