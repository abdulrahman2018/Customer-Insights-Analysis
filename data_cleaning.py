import pandas as pd

# Load the dataset with a different encoding
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='ISO-8859-1')  # or try 'latin1'
    print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
    return data

# Clean the data
def clean_data(data):
    # Remove rows with missing values in critical columns (e.g., 'InvoiceNo', 'CustomerID')
    data.dropna(subset=['InvoiceNo', 'CustomerID'], inplace=True)

    # Remove rows where quantity is less than 0 (returns, invalid transactions)
    data = data[data['Quantity'] > 0]

    # Remove duplicate rows
    data.drop_duplicates(inplace=True)

    print(f"Cleaned data: {data.shape[0]} rows and {data.shape[1]} columns.")
    return data

if __name__ == "__main__":
    file_path = '/Users/abdulrahmankhaled/Desktop/python/CustomerInsightsAnalysis/data/OnlineRetail.csv'
    retail_data = load_data(file_path)
    retail_data = clean_data(retail_data)
    print(retail_data.head())  # Display cleaned data
