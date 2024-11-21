import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    return data

# Perform EDA
def customer_analysis(data):
    # Convert 'InvoiceDate' to datetime format
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    # Calculate total spending per customer
    data['TotalSpend'] = data['Quantity'] * data['UnitPrice']
    customer_spending = data.groupby('CustomerID')['TotalSpend'].sum().reset_index()

    # Top 10 customers by spending
    top_10_customers = customer_spending.sort_values(by='TotalSpend', ascending=False).head(10)

    # Plot top 10 customers by spending
    plt.figure(figsize=(10, 6))
    sns.barplot(x='CustomerID', y='TotalSpend', data=top_10_customers)
    plt.title("Top 10 Customers by Spending")
    plt.xlabel("CustomerID")
    plt.ylabel("Total Spending")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    file_path = '/Users/abdulrahmankhaled/Desktop/python/CustomerInsightsAnalysis/data/OnlineRetail.csv'
    retail_data = load_data(file_path)
    retail_data = retail_data[retail_data['Quantity'] > 0]  # Clean data again
    customer_analysis(retail_data)
