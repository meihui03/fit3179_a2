import pandas as pd

# Load the CSV
df = pd.read_csv('data/blood_donations_state.csv')

# Filter for blood_type == "all"
df_filtered = df[df['blood_type'] == 'all']

# Aggregate donations by state
df_aggregated = df_filtered.groupby('state')['donations'].sum().reset_index()

# Save the preprocessed CSV
df_aggregated.to_csv('preprocessed_data.csv', index=False)
