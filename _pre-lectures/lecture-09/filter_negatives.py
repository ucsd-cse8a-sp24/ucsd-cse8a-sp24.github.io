def filter_negatives(nums):
    pnums = []
    for index in range(len(nums)):
        if nums[index] >= 0:
            pnums = pnums + [nums[index]]
    return pnums

def filter_negatives2(nums):
    pnums = []
    for n in nums:
        if n >= 0:
            pnums = pnums + [n]
    return pnums

def fill_list(num):
    pnums = []
    for index in range(num):
        pnums = pnums + [index]
    return pnums

def update_list(nums):
    #this is the way to update the contents of the list
    #using a loop
    for index in range(len(nums)):
        nums[index] = 0
    return nums

def update_list2(nums):
    for n in nums:
        #will not update the list (updates the variable n only)
        n = 0
    return nums
