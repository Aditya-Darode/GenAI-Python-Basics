nums  = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    check = {}                             #To store the number and its indices

    for i in range(len(nums)):
        complement = target - nums[i]      #What number do we need to reach the target
        if complement in check:            #looking if the required number is already seen in the dictionary(check)

            return [check[complement], i]  #Return the index of the complement and current number 
        check[nums[i]] = i                 #If not found, store the current number and its index in the dictionary
 
result = twoSum(nums, target)
print("Result: ",result)
