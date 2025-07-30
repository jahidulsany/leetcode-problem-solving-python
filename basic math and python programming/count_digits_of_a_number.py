import math

def count_digits(num: int) -> int :
    if num == 0:
        return 1
    else:
        return int(math.log10(abs(num)) + 1)


print(count_digits(num = 10067))