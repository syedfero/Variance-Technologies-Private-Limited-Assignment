import pandas as pd
import requests
def fetch_data(self):
    response = requests.get("<https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json>")
    # Converts JSON response to a Python dictionary
    data = response.json()
    # Converts dictionary to pandas DataFrame
    df = pd.DataFrame(data)
    # Save DataFrame to CSV
    df.to_csv('instruments.csv', index=False)  
def get_info_by_symbol(self, symbol):
    # Load data from CSV
    df = pd.read_csv('instruments.csv')
    # Filter rows
    filtered_df = df[df['symbol'] == symbol]  
    if not filtered_df.empty:
        # Return the first row of the filtered DataFrame
        return filtered_df.iloc[0]
    # Return None if no matching symbol is found
    return None  
