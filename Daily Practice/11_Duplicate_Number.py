'''You are given an array of integers nums containing n + 1 numbers where each number is in the range [1, n].
There is exactly one number that appears more than once.
Your task is to find and return this repeated number.

Do not modify the input array.
Use only constant extra space.
Time complexity should be better than O(n^2).'''

def findDuplicate(nums):
    # Initialize two pointers (slow and fast) at the first element
    slow = nums[0]
    fast = nums[0]

    # Move slow by 1 step and fast by 2 steps until they meet
    # This is the "cycle detection" phase
    while True:
        slow = nums[slow]              # move 1 step
        fast = nums[nums[fast]]        # move 2 steps

        if slow == fast:               # if they meet, cycle detected
            break

    # Reset slow to the start of the array (index 0)
    slow = nums[0]

    # Move both slow and fast one step at a time until they meet again
    # The meeting point is the duplicate number
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # Return the duplicate number
    return slow

nums = [3,1,3,4,2]
print(findDuplicate(nums))
