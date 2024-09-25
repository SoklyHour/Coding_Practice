import numpy as np

def find_outliers(sales):
    q1 = np.percentile(sales, 25)
    q3 = np.percentile(sales, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [sale for sale in sales if sale < lower_bound or sale > upper_bound]

# Example usage
sales = [100, 150, 200, 250, 300, 1000]  # 1000 is an outlier
print(find_outliers(sales))  # Output: [1000]
