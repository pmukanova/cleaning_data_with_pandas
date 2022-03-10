# Import process from fuzzywuzzy
from fuzzywuzzy import process
import pandas as pd

restaurants = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/cleaning_data_with_pandas/data/restaurants_L2_dirty.csv")

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants["cuisine_type"].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))