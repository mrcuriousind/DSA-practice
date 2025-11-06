
def longest_subarray_with_sum_k(nums, k):
    prefix_sum_map = {}  # stores: prefix_sum → first index where it occurred
    prefix_sum = 0
    max_length = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]  # running total

        # Case 1: If entire subarray from 0 to i sums to k
        if prefix_sum == k:
            max_length = i + 1
        




nums = [1, 2, 3, 1, 1, 1, 1, 2]
k = 4
longest_subarray_with_sum_k (nums, k)