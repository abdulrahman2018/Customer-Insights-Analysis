import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = '/Users/abdulrahmankhaled/Desktop/python/CustomerInsightsAnalysis/data/OnlineRetail.csv'
retail_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display missing values in each column
print("Missing values in each column:")
print(retail_data.isnull().sum())

# Clean data by removing rows with missing 'CustomerID'
retail_data_cleaned = retail_data.dropna(subset=['CustomerID'])

# Calculate 'TotalSales' as Quantity * UnitPrice
retail_data_cleaned['TotalSales'] = retail_data_cleaned['Quantity'] * retail_data_cleaned['UnitPrice']

# Group by StockCode to calculate total sales per product
product_sales = retail_data_cleaned.groupby('StockCode')['TotalSales'].sum().reset_index()

# Sort by TotalSales in descending order and take the top 10 products
top_products = product_sales.sort_values(by='TotalSales', ascending=False).head(10)

# Display the top 10 products
print("Top 10 products based on total sales:")
print(top_products)

# Save the top 10 products to a CSV file
top_products.to_csv('top_products.csv', index=False)

# Plot the top 10 products using a bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_products['StockCode'], top_products['TotalSales'], color='skyblue')
plt.xlabel('Total Sales')
plt.ylabel('StockCode')
plt.title('Top 10 Products Based on Total Sales')
plt.gca().invert_yaxis()  # Invert y-axis to display the highest sales on top
plt.show()
