import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('../data/donations_state.csv')

# Filter out rows where state is "Malaysia"
filtered_df = df[df['state'] != 'Malaysia']

# Calculate the total donations for location_centre and location_mobile
total_donations_location_centre = filtered_df['location_centre'].sum()
total_donations_location_mobile = filtered_df['location_mobile'].sum()

# Calculate the overall total donations
overall_total_donations = total_donations_location_centre + total_donations_location_mobile

# Calculate the percentage of total donations for each location
percentage_location_centre = (total_donations_location_centre / overall_total_donations) * 100 if overall_total_donations > 0 else 0
percentage_location_mobile = (total_donations_location_mobile / overall_total_donations) * 100 if overall_total_donations > 0 else 0

# Save the results to a new DataFrame
results_df = pd.DataFrame({
    "Location": ["Centre", "Mobile"],
    "Total Donations": [total_donations_location_centre, total_donations_location_mobile],
    "Percentage": [percentage_location_centre, percentage_location_mobile]
})

# Save the DataFrame to a CSV file
results_df.to_csv("../data/donation_results.csv", index=False)