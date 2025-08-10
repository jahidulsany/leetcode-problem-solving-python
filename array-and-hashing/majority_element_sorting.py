## Majority Element (Sorting)
# Find the majority element in an array using sorting.

def majority_element_sorting(nums: list[int]) -> int:
    nums.sort()
    mid = len(nums) // 2
    return nums[mid]    # time complexity: O(n log n)

print(majority_element_sorting(nums = [1,1,2,2,1,2,2]))