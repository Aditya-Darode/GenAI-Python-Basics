def subarraySum(nums, k):
    # total_count will store the number of subarrays that sum to k
    total_count = 0

    # prefix_sum keeps the running sum of elements from start to current index
    prefix_sum = 0

    # count_map stores how many times each prefix sum has occurred
    # Initialize with {0:1} to handle subarrays starting from index 0
    count_map = {0: 1}

    
    for num in nums:
        prefix_sum += num  # update the running sum

        # if (prefix_sum - k) exists in count_map, 
        # it means there is a previous subarray that sums to k
        if (prefix_sum - k) in count_map:
            total_count += count_map[prefix_sum - k]

        # update the count_map with current prefix_sum
        if prefix_sum in count_map:
            count_map[prefix_sum] += 1
        else:
            count_map[prefix_sum] = 1

    return total_count


nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  # Output: 2
