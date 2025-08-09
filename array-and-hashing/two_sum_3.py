### Two Sum Problem
### Given an array of integers and a target sum, find two numbers in the array that add up to the target sum.

## Optimized Solution using HashMap

def two_sum(nums: list[int], target: int) -> list[int]:
    visited = {}  # store seen numbers and their indices {num: index}
    
    for i, num in enumerate(nums):  # i = index, num = value at that index
        needed = target - num       # the number we need to find a match
        if needed in visited:       # have we seen the needed number before?
            return [visited[needed], i]  # return the earlier index and current index
        visited[num] = i            # remember the current number and index
    return [] 


print(two_sum(nums=[1, 2, 3, 4], target=8))  # no match found
print(two_sum(nums=[11, 7, 2, 15], target=9))  # Output: [1, 2]