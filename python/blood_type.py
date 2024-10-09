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

# Calculate the total donations across all blood types
total_donations = total_blood_a + total_blood_b + total_blood_o + total_blood_ab

# Calculate the percentage for each blood type
percentage_blood_a = (total_blood_a / total_donations) * 100
percentage_blood_b = (total_blood_b / total_donations) * 100
percentage_blood_o = (total_blood_o / total_donations) * 100
percentage_blood_ab = (total_blood_ab / total_donations) * 100

# Print the results
print(f"Total Donations for Blood Type A: {total_blood_a} ({percentage_blood_a:.2f}%)")
print(f"Total Donations for Blood Type B: {total_blood_b} ({percentage_blood_b:.2f}%)")
print(f"Total Donations for Blood Type O: {total_blood_o} ({percentage_blood_o:.2f}%)")
print(f"Total Donations for Blood Type AB: {total_blood_ab} ({percentage_blood_ab:.2f}%)")

# Alternatively, save the results into a DataFrame and export as a CSV
results_df = pd.DataFrame({
    "Blood Type": ["A", "B", "O", "AB"],
    "Total Donations": [total_blood_a, total_blood_b, total_blood_o, total_blood_ab],
    "Percentage": [percentage_blood_a, percentage_blood_b, percentage_blood_o, percentage_blood_ab]
})

# Save to a new CSV file
results_df.to_csv('../data/total_donations_by_blood_type.csv', index=False)
