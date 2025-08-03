### Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums: list[int]) -> int:
    # Using a hashmap to count occurrences of each element
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] = count_map[num] + 1
     
    ## Evaluation
    for num,count in  count_map.items():
        if count > (len(nums)/2):
            return num
    return 0


print(majorityElement(nums = [3,2,3])) 
print(majorityElement(nums = [2,2,1,1,1,2,2]))