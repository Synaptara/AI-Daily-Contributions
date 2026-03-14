def find_pair(nums):
    # find the target sum in the list
    target_sum = nums[-1]
    nums = nums[:-1]
    
    # create a set to store the numbers we have seen so far
    seen = set()
    
    # iterate over the list
    for num in nums:
        # calculate the complement of the current number
        complement = target_sum - num
        
        # if the complement is in the set, return the pair
        if complement in seen:
            return [complement, num]
        
        # add the current number to the set
        seen.add(num)
    
    # if no pair is found, return None
    return None