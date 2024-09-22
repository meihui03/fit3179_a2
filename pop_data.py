import pandas as pd

# Load preprocessed_data.csv
preprocessed_df = pd.read_csv('data/preprocessed_data.csv')

# Load population.csv
population_df = pd.read_csv('data/population.csv')

# Merge the dataframes on the 'state' column
# This will add the 'pop' column from population_df to preprocessed_df
merged_df = pd.merge(preprocessed_df, population_df[['state', 'pop']], on='state', how='left')

# Check if there are any states without population data
missing_pop = merged_df[merged_df['pop'].isnull()]
if not missing_pop.empty:
    print(f"Warning: Some states are missing population data: \n{missing_pop['state']}")

# Save the merged dataframe back to preprocessed_data.csv
merged_df.to_csv('data/preprocessed_data.csv', index=False)

print("Preprocessed data updated with population column.")