import pandas as pd

airlines = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/cleaning_data_with_pandas/data/airlines_final.csv")

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

