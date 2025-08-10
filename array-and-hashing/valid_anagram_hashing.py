## given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_count_map = {}
    t_count_map = {}

    for char in s:
        # if char in s_count_map:
        #     s_count_map[char] += 1
        # else:
        #     s_count_map[char] = 1
        s_count_map[char] = s_count_map.get(char, 0) + 1

    for char in t:
        # if char in t_count_map:
        #     t_count_map[char] += 1
        # else:
        #     t_count_map[char] = 1
        t_count_map[char] = t_count_map.get(char, 0) + 1

    return s_count_map == t_count_map

print(isAnagram(s = "anagram", t= "nagaram"))
print(isAnagram(s = "car", t= "rat"))