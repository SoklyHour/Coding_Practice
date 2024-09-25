def longest_common_substring(text1, text2):
    """Finds the longest common substring in two strings."""
    
    m = len(text1)
    n = len(text2)

    # Create a 2D DP array
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Variable to track the length of the longest common substring
    longest = 0
    end_index = 0  # To track where the longest substring ends in text1

    # Find the length of the longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    end_index = i  # Update the end index for substring extraction
            else:
                dp[i][j] = 0  # No common substring
    
    # Construct the longest common substring based on the DP table
    substring = text1[end_index - longest:end_index] if longest > 0 else ""

    return substring

# Example usage
text1 = "GeeksforGeeks"
text2 = "GeeksQuiz"
result = longest_common_substring(text1, text2)
print(f"The longest common substring is: '{result}'")
