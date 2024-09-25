import pandas as pd 
def add_double_column(df, column):
    df[f'Double_{column}'] = df[column] * 2
    return df

# Example usage
df = pd.DataFrame({'A': [1, 2, 3]})
print(add_double_column(df, 'A'))
