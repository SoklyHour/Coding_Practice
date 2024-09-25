# How do you find the non-matching characters in a string?

# You can detect different characters in two equally long strings by 
# comparing their corresponding characters and noting discrepancies.

def find_non_matching(str1, str2):
    non_matching = []
    for i in  range(len(str1)): 
        if str1[i] != str2[i]:
            non_matching.append(i)
    return non_matching

print(find_non_matching("hello", "hallo"))  # Output: [1]
print(find_non_matching("abcde", "abfgh"))  # Output: [2, 3, 4]
print(find_non_matching("12345", "12345"))  # Output: []