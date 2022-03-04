import pandas as pd

ride_sharing = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/cleaning_data_with_pandas/data/ride_sharing_new.csv")

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())