import pandas as pd

ride_sharing = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/cleaning_data_with_pandas/data/ride_sharing_new.csv")
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())