def calculate_retention_rate(year1_customers, year2_customers):
    retained_customers = len(set(year1_customers) & set(year2_customers))
    return retained_customers / len(year1_customers) * 100 if year1_customers else 0

# Example usage
year1_customers = ['Alice', 'Bob', 'Charlie']
year2_customers = ['Bob', 'Charlie', 'David']
print(calculate_retention_rate(year1_customers, year2_customers))  # Output: 66.66666666666666
