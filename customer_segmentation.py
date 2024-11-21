import pandas as pd

# Correct file path to your dataset
file_path = '/Users/abdulrahmankhaled/Desktop/python/CustomerInsightsAnalysis/data/OnlineRetail.csv'

# Load the dataset
retail_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display basic information about the dataset
print("Data loaded successfully with", retail_data.shape[0], "rows and", retail_data.shape[1], "columns.")

# Check for any missing values
missing_values = retail_data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Drop any rows with missing customer IDs
retail_data = retail_data.dropna(subset=['CustomerID'])

# Drop duplicates if any
retail_data.drop_duplicates(inplace=True)

# Cleaned data info
print("\nCleaned data:", retail_data.shape[0], "rows and", retail_data.shape[1], "columns.")

# Segment the data into different customer segments based on the total spending
# First, calculate the total spending per customer
retail_data['Total_Spending'] = retail_data['Quantity'] * retail_data['UnitPrice']

# Group by CustomerID to get total spending per customer
customer_spending = retail_data.groupby('CustomerID').agg({'Total_Spending': 'sum'}).reset_index()

# Create customer segments based on spending
# This is just an example; segments can vary based on your analysis
def customer_segment(spending):
    if spending < 50:
        return 'Low Spend'
    elif spending < 200:
        return 'Medium Spend'
    else:
        return 'High Spend'

# Apply the segmentation
customer_spending['Segment'] = customer_spending['Total_Spending'].apply(customer_segment)

# Display the segmentation results
print("\nCustomer segmentation based on total spending:")
print(customer_spending.head())

# Optionally, save the results to a new CSV file
customer_spending.to_csv('/Users/abdulrahmankhaled/Desktop/python/CustomerInsightsAnalysis/data/customer_segments.csv', index=False)

print("\nCustomer segmentation data saved to 'customer_segments.csv'")
