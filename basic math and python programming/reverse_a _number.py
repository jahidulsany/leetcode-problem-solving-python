import math

def reverse_number(num : int) -> int:
    construct_num = 0

    while num != 0:
        last_digit = int(math.fmod(num, 10))
        construct_num = (construct_num * 10) + last_digit
        num = int(num / 10)
    return construct_num
    

print(reverse_number(num = 62958653))



