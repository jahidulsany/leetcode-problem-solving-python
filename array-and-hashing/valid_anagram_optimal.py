## given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word

## Optimal Approach

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # Assuming only lowercase letters a-z

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    # If all counts are zero, it's an anagram
    # for i in range(26):
    #     if count[i] != 0:
    #         return False
    # return True

    return all(c == 0 for c in count)

print(isAnagram(s = "anagram", t= "nagaram"))
print(isAnagram(s = "car", t= "arc"))
print(isAnagram(s = "rat", t= "car"))