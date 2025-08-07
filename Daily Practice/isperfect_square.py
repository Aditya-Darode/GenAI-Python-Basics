# Program to check whether a number is a perfect square using binary search

num = int(input("Enter a number: "))

def isPerfectSquare(num):
    if num < 0:          # Negative numbers cannot be perfect squares
        return False

    if num == 0 or num == 1: # Edge case: 0 and 1 are perfect squares
        return True
    
    left = 2
    right = num // 2

    while left <= right:           # Binary search loop
        mid = (left + right) // 2  # Find the middle value

        if mid * mid == num:       # Check if mid*mid equals the number
            return True
        elif mid * mid < num:      # If mid*mid is less than num, search in the right half
            left = mid + 1
        else:
            right = mid - 1        # If mid*mid is greater than num, search in the left half
    return False
print(isPerfectSquare(num))
