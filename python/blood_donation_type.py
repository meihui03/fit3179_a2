import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('../data/donations_state.csv')

# Filter out rows where state is "Malaysia"
filtered_df = df[df['state'] != 'Malaysia']

# Sum the donations for each blood donation type
total_donations_wholeblood = filtered_df['type_wholeblood'].sum()
total_donations_platelet = filtered_df['type_apheresis_platelet'].sum()
total_donations_plasma = filtered_df['type_apheresis_plasma'].sum()
total_donations_other = filtered_df['type_other'].sum()

# Calculate the overall total donations across all types
overall_total_donations = (total_donations_wholeblood + 
                           total_donations_platelet + 
                           total_donations_plasma + 
                           total_donations_other)

# Calculate the percentage of total donations for each donation type
percentage_wholeblood = (total_donations_wholeblood / overall_total_donations) * 100 if overall_total_donations > 0 else 0
percentage_platelet = (total_donations_platelet / overall_total_donations) * 100 if overall_total_donations > 0 else 0
percentage_plasma = (total_donations_plasma / overall_total_donations) * 100 if overall_total_donations > 0 else 0
percentage_other = (total_donations_other / overall_total_donations) * 100 if overall_total_donations > 0 else 0

# Save the results to a new DataFrame
results_df = pd.DataFrame({
    "Blood Donation Type": ["Whole Blood", "Apheresis Platelet", "Apheresis Plasma", "Other"],
    "Total Donations": [total_donations_wholeblood, total_donations_platelet, total_donations_plasma, total_donations_other],
    "Percentage": [percentage_wholeblood, percentage_platelet, percentage_plasma, percentage_other]
})

# Save the DataFrame to a CSV file
results_df.to_csv("../data/donation_results_by_type.csv", index=False)
