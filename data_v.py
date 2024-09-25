import pandas as pd  # Make sure to import pandas
import matplotlib.pyplot as plt

def plot_value_counts(df, column):
    counts = df[column].value_counts()
    counts.plot(kind='bar')
    plt.title(f'Counts of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

# Example usage
df = pd.DataFrame({'A': ['a', 'b', 'a', 'c', 'b']})  # Use pandas to create the DataFrame
plot_value_counts(df, 'A')

