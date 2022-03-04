import pandas as pd

airlines = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/cleaning_data_with_pandas/data/airlines_final.csv")

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])