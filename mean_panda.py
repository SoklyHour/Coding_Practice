import pandas as pd
def calculate_mean(df, column):
    return df[column].mean()

# Example usage
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
print(calculate_mean(df, 'A'))  # Output: 3.0