## Majority Element - Boyer-Moore Voting Algorithm
# This algorithm finds the majority element in an array using a linear time complexity and constant space complexity.

def majorityElement(nums: list[int]) -> int:
    candiate = -1
    count = 0

    for num in nums:
        if count == 0:
            candiate = num
            count = 1
        elif num == candiate:
            count += 1
        else:
            count -= 1
    return candiate

print(majorityElement(nums = [3,2,3]))
print(majorityElement(nums = [2,2,1,1,1,2,2]))
print(majorityElement(nums = [1,2,3,3,1,2,2,3,3,3,3]))
