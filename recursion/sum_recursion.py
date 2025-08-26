## Sum of n natural numbers

def sum_n(n: int) -> int:
    if n == 0:
        return 0
    res = n + sum_n(n-1)
    return res

print(sum_n(7))  # Output: 28