# Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.  

### Two Sum Problem

def two_sum(nums, target):
    visited = {}
    for i in range(0, len(nums)):
        current = nums[i]
        reminder = target - current
        if reminder in visited:
            return [visited[reminder], i]
        visited[current] = i
    return []

print(two_sum(nums=[11, 2, 15, 7], target=9)) # Output: [1, 3]