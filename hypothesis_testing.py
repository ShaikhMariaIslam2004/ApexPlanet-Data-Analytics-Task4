import pandas as pd
from scipy import stats

# Load the Task 3 dashboard dataset
df = pd.read_csv("task3_dashboard_data.csv")

# Pearson correlation test
correlation, p_value = stats.pearsonr(
    df["Quantity"],
    df["Total_Sales"]
)

print("Correlation:", correlation)
print("P-value:", p_value)

# Results from the test
# Correlation: 0.6466406163004241
# P-value: 1.713608108961374e-119
#
# Interpretation:
# Since the p-value is much smaller than 0.05, the null hypothesis
# is rejected. The result provides strong statistical evidence of
# a positive linear relationship between Quantity and Total Sales.
# This indicates an association and does not establish causation.
