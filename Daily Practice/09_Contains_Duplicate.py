'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

def containsDuplicate(nums):
    # Create an empty set to store numbers we have already seen
    seen = set()

    for num in nums:
        # If the number is already in 'seen', it means duplicate found
        if num in seen:
            return True   # Return True immediately
        else:
            # Otherwise, add the number to the set
            seen.add(num)
    return False

nums = [1, 2, 3, 1]      #Output : True 
#nums = [1, 2, 3, 4]     #Output : False
print(containsDuplicate(nums))