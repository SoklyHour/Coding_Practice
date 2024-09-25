def calculate_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Both lists must have the same length.")
    return np.corrcoef(x, y)[0, 1]

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
print(calculate_correlation(x, y))  # Output: 1.0 (perfect correlation)
