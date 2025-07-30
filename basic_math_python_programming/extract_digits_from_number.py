### Extract digits from a number and return a list or array

def extract_digits(num : int) -> int:
    res = []
    while num > 0: 
        last_digit = num % 10 
        res.append(last_digit)
        num = int(num / 10)
    res.reverse()
    return res

print(extract_digits(num = 843824))
