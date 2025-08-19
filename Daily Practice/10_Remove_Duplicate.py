'''Given a sorted array nums, remove duplicates in-place so that each unique element appears only once.
Return the count k of unique elements, and modify nums so the first k elements contain those unique values.

Example:
Input: [1,1,2] → Output: k=2, nums=[1,2,_]
Input: [0,0,1,1,1,2,2,3,3,4] → Output: k=5, nums=[0,1,2,3,4,_,_,_,_,_]'''

def removeDuplicate(nums):
    if not nums:   # If array is empty
        return 0
    
    # i points to last unique element
    i = 0
    for j in range(1, len(nums)):

        # If nums[j] is new (not equal to last unique)
        if nums[j] != nums[i]:
            i += 1               # Move i forward
            nums[i] = nums[j]    # Copy unique element here

    return i + 1                 # Number of unique elements = i + 1
        
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate(nums))
