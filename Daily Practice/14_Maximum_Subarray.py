'''Given an integer array nums, find the subarray with the largest sum, and return its sum
Kadane’s Algorithm is a Dynamic Programming technique used to solve the problem'''

def maximumSubarray(nums):
    # Initialize variables
    # current_sum > best sum of subarray ending at current index
    # max_sum > best sum found overall
    current_sum = nums[0]    # start with the first element
    max_sum = nums[0]        # also set max_sum to first element

    for i in range(1, len(nums)):

        # Either extend the previous subarray OR start a new subarray from nums[i]
        current_sum = max(nums[i], current_sum + nums[i])

        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
  
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]  #Output : 6
print(maximumSubarray(nums))



