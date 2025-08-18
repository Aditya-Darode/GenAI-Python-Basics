"""
Problem Statement:
We have a sorted list where every number appears exactly twice, except for one number
that appears only once. We need to find and print that single number and stop 
as soon as we find it.

Example:
Input:  [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
Output: Single number is:  2
"""

numbers = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]

for i in range(0, len(numbers), 2):  # Loop through the list in steps of 2 because pairs are adjacent
    
    # Case 1: If we're at the last element in the list (odd length case)
    # Case 2: Or if the current element is not equal to the next one
    if i == len(numbers) - 1 or numbers[i] != numbers[i + 1]:
        
        print("Single number is:", numbers[i]) # This is the single element without a duplicate
        break



# One more way to solve this problem by using XOR operation
# XOR of a number with itself is 0 (e.g., 4 ^ 4 = 0)
# XOR of a number with 0 is the number itself (e.g., 0 ^ 5 = 5)
# Since all pairs cancel out to 0, the result after XORing all numbers will be the single number.
numbers = [1,1,2,3,3,4,4,5,5,6,6]
single = 0

for i in numbers:
    single ^= i
print("Single number is: ", single)

