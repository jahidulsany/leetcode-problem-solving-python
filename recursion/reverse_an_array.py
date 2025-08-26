## Reverse an array using recursion

def swap(arr: list[int], left: int, right: int):
    if left <= right:
        temp_right = arr[right]
        arr[right] = arr[left]
        arr[left] = temp_right

        swap(arr, left = left + 1, right = right - 1)
        

def reverse_array(nums: list[int]):
    swap(nums, left = 0, right = len(nums) - 1)
    return nums

nums = [1, 2, 3, 4, 5]
print(reverse_array(nums))