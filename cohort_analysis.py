import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/abdulrahmankhaled/Desktop/python/CustomerInsightsAnalysis/data/OnlineRetail.csv'
retail_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert the 'InvoiceDate' column to datetime
retail_data['InvoiceDate'] = pd.to_datetime(retail_data['InvoiceDate'])

# Drop rows with missing 'CustomerID'
retail_data = retail_data.dropna(subset=['CustomerID'])

# Extract year and month from the 'InvoiceDate' to create cohorts
retail_data['InvoiceYearMonth'] = retail_data['InvoiceDate'].dt.to_period('M')

# Create a cohort group for each customer based on their first purchase date
cohort_data = retail_data.groupby('CustomerID').agg({'InvoiceDate': 'min'}).reset_index()
cohort_data['FirstPurchaseDate'] = cohort_data['InvoiceDate'].dt.to_period('M')

# Merge cohort data back with the retail data to get the cohort for each purchase
retail_data = retail_data.merge(cohort_data[['CustomerID', 'FirstPurchaseDate']], on='CustomerID')

# Calculate the cohort index (number of months since first purchase)
retail_data['CohortIndex'] = (retail_data['InvoiceDate'].dt.to_period('M').astype('int64') - 
                              retail_data['FirstPurchaseDate'].astype('int64'))

# Now, pivot the data to get the cohort retention matrix
cohort_counts = retail_data.pivot_table(index='FirstPurchaseDate', 
                                       columns='CohortIndex', 
                                       values='CustomerID', 
                                       aggfunc=pd.Series.nunique)

# Calculate the retention rate by dividing each cohort's count by the first month's count
cohort_size = cohort_counts.iloc[:, 0]  # The size of the first cohort (first month)
cohort_retention = cohort_counts.divide(cohort_size, axis=0)

# Fill NaN values with 0 (indicating no customers in those months)
cohort_retention = cohort_retention.fillna(0)

# Plotting the cohort retention heatmap using Matplotlib and Seaborn
plt.figure(figsize=(12, 8))
sns.heatmap(cohort_retention, annot=True, fmt=".0%", cmap="YlGnBu", cbar=True)

# Set labels and title for the heatmap
plt.title('Cohort Retention Analysis', fontsize=16)
plt.xlabel('Cohort Month', fontsize=12)
plt.ylabel('First Purchase Date', fontsize=12)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Show the plot
plt.show()

# Save the heatmap as a .png image
plt.savefig('cohort_retention_heatmap.png')
