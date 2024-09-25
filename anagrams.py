def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Test cases
test_cases = [
    ("listen", "silent"),
    ("triangle", "integral"),
    ("apple", "pale"),
    ("evil", "vile"),
    ("fluster", "restful"),
    ("night", "thing"),
    ("hello", "world"),
]

# Print results
for s1, s2 in test_cases:
    result = are_anagrams(s1, s2)
    print(f"Are '{s1}' and '{s2}' anagrams? {result}")