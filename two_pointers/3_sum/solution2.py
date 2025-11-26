def three_sum(nums):
    l = nums
    list.sort(l)
    triplets = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            k = j + 1
            s = set(l[k:])
            val = -1*l[i] - 1*l[j]
            if val in s:
                item = (l[i], l[j], val)
                triplets.add(item)
    return list(triplets)
