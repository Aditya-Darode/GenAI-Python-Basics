#You are given a sorted array numbers and a target.
#Find two numbers such that they add up to target. Return their indices (1-based).
#Here i have used two pointer technique: one at start and one at end, move inward.

def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left < right:
        s = numbers[left] + numbers[right]  #Add the two numbers pointed by left and right.
        if s == target:
            return [left+1, right+1]        #Return the 1-based indices → left+1, right+1
        elif s < target:
            left +1                         #f the sum is too small, move left rightwards to increase the sum.
        else:
            right -=1                       #If the sum is too big, move right leftwards to decrease the sum.

numbers = [2, 7, 11, 15]
target = 9

result = twoSum(numbers, target)
print("Result : ", result)