def calculate_monthly_growth_rate(monthly_sales):
    growth_rates = []
    for i in range(1, len(monthly_sales)):
        growth_rate = (monthly_sales[i] - monthly_sales[i-1]) / monthly_sales[i-1] * 100
        growth_rates.append(growth_rate)
    return growth_rates

# Example usage
monthly_sales = [100, 120, 150, 180]
print(calculate_monthly_growth_rate(monthly_sales))  # Output: [20.0, 25.0, 20.0]
