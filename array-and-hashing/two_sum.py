### Two Sum Problem
### Given an array of integers and a target sum, find two numbers in the array that add up to the target sum.

############### BRUTE FORCE SOLUTION #############

## Time Complexity: O(n^2) ## Space Complexity: O(1)
## This solution uses a brute force approach to check all pairs of numbers.

def two_sum(nums: list[int], target: int) -> list[int] | None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(two_sum(nums=[15, 7, 11, 2], target=9)) # Output: [1, 3]