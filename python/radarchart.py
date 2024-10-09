import pandas as pd

# Load the dataset
df = pd.read_csv('../data/donations_state.csv')

# Filter the dataset to only include rows where the state is 'Malaysia'
malaysia_df = df[df['state'] == 'Malaysia']

# Prepare a DataFrame for blood donations grouped by location (centre or mobile) and blood type
preprocessed_data = pd.DataFrame({
    'Blood_Type': ['A', 'B', 'O', 'AB', 'A', 'B', 'O', 'AB'],
    'Location': ['Centre', 'Centre', 'Centre', 'Centre', 'Mobile', 'Mobile', 'Mobile', 'Mobile'],
    'Total_Donations': [
        malaysia_df[malaysia_df['location_centre'] > 0]['blood_a'].sum(),
        malaysia_df[malaysia_df['location_centre'] > 0]['blood_b'].sum(),
        malaysia_df[malaysia_df['location_centre'] > 0]['blood_o'].sum(),
        malaysia_df[malaysia_df['location_centre'] > 0]['blood_ab'].sum(),
        malaysia_df[malaysia_df['location_mobile'] > 0]['blood_a'].sum(),
        malaysia_df[malaysia_df['location_mobile'] > 0]['blood_b'].sum(),
        malaysia_df[malaysia_df['location_mobile'] > 0]['blood_o'].sum(),
        malaysia_df[malaysia_df['location_mobile'] > 0]['blood_ab'].sum()
    ]
})

# Save the preprocessed data to a CSV file
preprocessed_data.to_csv('../data/preprocessed_donations_for_radar_chart.csv', index=False)

# Display the preprocessed data
print(preprocessed_data)
