import pandas as pd
import missingno as msno

banking = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/cleaning_data_with_pandas/data/banking_dirty.csv")

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])