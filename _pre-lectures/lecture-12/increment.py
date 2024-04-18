#modify the existing list (num)
def incr_mod(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 1

#return a new list, don't change num
def incr_new(nums):
    res = nums[:]
    for i in range(len(res)):
        res[i] = res[i] + 1
    return res
