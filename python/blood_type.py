import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('../data/donations_state.csv')

# Filter the dataset to only include rows where the state is 'Malaysia'
malaysia_df = df[df['state'] == 'Malaysia']

# Calculate the total donations for each blood type
total_blood_a = malaysia_df['blood_a'].sum()
total_blood_b = malaysia_df['blood_b'].sum()
total_blood_o = malaysia_df['blood_o'].sum()
total_blood_ab = malaysia_df['blood_ab'].sum()

# Print the results
print(f"Total Donations for Blood Type A: {total_blood_a}")
print(f"Total Donations for Blood Type B: {total_blood_b}")
print(f"Total Donations for Blood Type O: {total_blood_o}")
print(f"Total Donations for Blood Type AB: {total_blood_ab}")

# Alternatively, save the results into a DataFrame and export as a CSV
results_df = pd.DataFrame({
    "Blood Type": ["A", "B", "O", "AB"],
    "Total Donations": [total_blood_a, total_blood_b, total_blood_o, total_blood_ab]
})

# Save to a new CSV file
results_df.to_csv('../data/total_donations_by_blood_type.csv', index=False)
