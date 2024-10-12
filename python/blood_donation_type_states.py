import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('../data/donations_state.csv')

# Filter out rows where state is not "Malaysia"
filtered_df = df[df['state'] != 'Malaysia']

# Group by 'state' and calculate the sum of donations for each blood donation type
grouped_df = filtered_df.groupby('state').agg({
    'type_wholeblood': 'sum',
    'type_apheresis_platelet': 'sum',
    'type_apheresis_plasma': 'sum',
    'type_other': 'sum'
}).reset_index()

# Calculate the overall total donations for each state
grouped_df['overall_total_donations'] = (grouped_df['type_wholeblood'] + 
                                         grouped_df['type_apheresis_platelet'] + 
                                         grouped_df['type_apheresis_plasma'] + 
                                         grouped_df['type_other'])

# Calculate the percentage of total donations for each blood donation type for each state
grouped_df['percentage_wholeblood'] = (grouped_df['type_wholeblood'] / grouped_df['overall_total_donations']) * 100
grouped_df['percentage_platelet'] = (grouped_df['type_apheresis_platelet'] / grouped_df['overall_total_donations']) * 100
grouped_df['percentage_plasma'] = (grouped_df['type_apheresis_plasma'] / grouped_df['overall_total_donations']) * 100
grouped_df['percentage_other'] = (grouped_df['type_other'] / grouped_df['overall_total_donations']) * 100

# Reshape the DataFrame to have a row for each state and blood donation type
results_df = pd.melt(
    grouped_df,
    id_vars=['state', 'overall_total_donations'],
    value_vars=['type_wholeblood', 'type_apheresis_platelet', 'type_apheresis_plasma', 'type_other'],
    var_name='Blood Donation Type',
    value_name='Total Donations'
)

# Map the variable names to more readable labels for blood donation types
results_df['Blood Donation Type'] = results_df['Blood Donation Type'].replace({
    'type_wholeblood': 'Whole Blood',
    'type_apheresis_platelet': 'Apheresis Platelet',
    'type_apheresis_plasma': 'Apheresis Plasma',
    'type_other': 'Other'
})

# Add the percentage values to the results DataFrame
results_df['Percentage'] = pd.melt(
    grouped_df,
    id_vars=['state'],
    value_vars=['percentage_wholeblood', 'percentage_platelet', 'percentage_plasma', 'percentage_other'],
    value_name='Percentage'
)['Percentage']

# Save the results to a new CSV file
results_df.to_csv("../data/donation_results_by_state_and_type.csv", index=False)

print("The data has been aggregated and saved into 'donation_results_by_state_and_type.csv'")
