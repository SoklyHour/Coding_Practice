# How do you find out if the two given strings are anagrams?
# Two strings are anagrams if they have the same characters in a different order.
# You can sort the characters in each string and compare them.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("triangle", "integral"))  # Output: True
print(are_anagrams("apple", "pale"))  # Output: False
print(are_anagrams("anagram", "nagaram"))  # Output: True
print(are_anagrams("aa","aa"))
print(are_anagrams("sa","as"))
print(are_anagrams("11",'11'))
print(are_anagrams("sa","aa"))