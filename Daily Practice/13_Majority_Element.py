'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

def majorityElement(nums):
    # Create an empty dictionary to store frequency of each element
    dic = { }

    for num in nums:
        # dic.get(num, 0) → if num exists, get its count; if not, default to 0
        # then add 1 to update the frequency
        dic[num] = dic.get(num, 0) + 1

        # As soon as we find an element whose count > n/2, return it
        if dic[num] > len(nums)//2:
            return num
        
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
#O(n) time, O(k) space.



'''This is Boyer-Moore Voting Algorithm Method it '''
# def majorityElement(nums):
#     # Initialize candidate and counter
#     candidate = None
#     count = 0

#     # Traverse through the list
#     for num in nums:
#         if count == 0:
#             # If count is zero, choose the current number as new candidate
#             candidate = num
#         # If current number is same as candidate, increase count
#         # Otherwise, decrease count
#         count += (1 if num == candidate else -1)

#     # The candidate left after cancellation is the majority element
#     return candidate
#O(n) time, O(1) space