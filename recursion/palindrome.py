## Palindrome 
## Return True if the given string is a Palindrome or vice-versa

def is_palindrome(s:str, left: int, right: int) -> bool:
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return is_palindrome(s, left = left + 1, right = right - 1)

def check_palindrome(s:str):
    is_pal = is_palindrome(s, left = 0, right = len(s) - 1)
    print(f"{s} is a palindrom: {is_pal}")
    return is_pal

print(check_palindrome("madam"))
print(check_palindrome("sir"))
print(check_palindrome("noon"))
print(check_palindrome("abda"))
    