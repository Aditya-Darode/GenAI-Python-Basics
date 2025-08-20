'''Given an array of integers nums, return the pivot index of this array.

The pivot index is the index where the sum of all numbers strictly to the left of the index is equal to the sum of all numbers strictly to the right of the index.
If the pivot index exists, return the leftmost pivot index.
If no such index exists, return -1.'''

def pivotIndex(nums):
    totalSum = sum(nums)

    # Initialize left sum as 0 (before the loop starts)
    leftSum = 0

    for i in range(len(nums)):
        # Calculate right sum using formula
        rightSum = totalSum - leftSum - nums[i]

        # If left sum equals right sum -> pivot found
        if leftSum == rightSum:
            return i             # return the pivot index
        else:
            # Update left sum for the next iteration
            leftSum += nums[i]

    return -1

nums = [1,7,3,6,5,6]  #Output : 3
print(pivotIndex(nums))