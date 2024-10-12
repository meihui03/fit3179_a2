import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv('../data/newdonors_state.csv')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Create new 'year' and 'month' columns from the 'date'
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Melt the DataFrame to bring all age groups into a single column 'age_group'
df_melted = df.melt(id_vars=['year', 'month', 'state'], 
                    value_vars=['17-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64'], 
                    var_name='age_group', 
                    value_name='donations')

# Group by 'year', 'month', 'age_group', and 'state' and sum up the donations
df_grouped = df_melted.groupby(['year', 'month', 'age_group', 'state'])['donations'].sum().reset_index()

# Save the aggregated data to a new CSV file
df_grouped.to_csv('../data/newdonors_state_aggregated_by_month.csv', index=False)

print("The data has been aggregated by month and saved into 'newdonors_state_aggregated_by_month.csv'")
