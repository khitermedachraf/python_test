import os

import pandas as pd
import numpy as np
# We need also to install the 'openpyxl' module which is required for reading Excel files:  pip install openpyxl
import re


def sanitize_file_name(file_name):
    # Remove special characters from the file name
    return re.sub(r'[\\/*?:"<>|]', '', file_name)


def convert_to_pln(df):
    # Load FXrates.csv into a DataFrame
    fx_rates = pd.read_csv('FXrates.csv')

    # Filter FX rates for EUR to USD and PLN to USD
    eur_to_usd_rate = fx_rates.loc[fx_rates['Currency'] == 'EUR', 'Per USD'].values[0]
    pln_to_usd_rate = fx_rates.loc[fx_rates['Currency'] == 'PLN', 'Per USD'].values[0]

    # Convert Amount from EUR to PLN using USD as an intermediate currency
    df['Amount_USD'] = df['Amount'] / eur_to_usd_rate
    df['Amount_PLN'] = df['Amount_USD'] * pln_to_usd_rate
    # Drop unnecessary columns
    df = df.drop(columns=['Amount_USD'])

    return df


def save_files_by_type(df):
    # Create a folder named 'results' if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')

    # Get unique Type values
    unique_types = df['Type'].unique()

    # Iterate over unique Type values
    for type_val in unique_types:
        # Filter DataFrame for the current Type value
        filtered_df = df[df['Type'] == type_val]

        # Sanitize the Type value for constructing the file name
        sanitized_type = sanitize_file_name(type_val)

        # Define the file name with the sanitized Type value
        file_name = f"Table_{sanitized_type}.xlsx"

        # Save the filtered DataFrame to an Excel file in the 'results' folder
        filtered_df.to_excel(os.path.join('results', file_name), index=False)


def task_1():
    # Get a list of all files matching the pattern 'Table_*'
    file_list = [file for file in os.listdir() if file.startswith('Table_')]

    # Load each file into a Pandas DataFrame
    dfs = []
    for file in file_list:
        if file.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            continue  # Skip files with unsupported extensions
        dfs.append(df)

    # Merge all DataFrames into a single DataFrame
    merged_df = pd.concat(dfs, ignore_index=True)

    # Drop duplicates from the merged DataFrame if any
    merged_df = merged_df.drop_duplicates()

    # Show the number of null values in each column
    null_counts = merged_df.isnull().sum()
    print("Number of null values in each column:")
    print(null_counts)

    # Fill numerical null values with 1337
    merged_df = merged_df.fillna(1337)

    # Convert "Acctg Date" and "Date" columns to datetime objects
    merged_df['Acctg Date'] = pd.to_datetime(merged_df['Acctg Date'])
    merged_df['Date'] = pd.to_datetime(merged_df['Date'])

    # Define UK bank holidays as strings in the format 'dd/mm/yyyy'
    uk_bank_holidays = [
        '01/01/2022',
        '15/04/2022',
        '18/04/2022',
        '02/05/2022',
        '02/06/2022',
        '29/08/2022',
        '25/12/2022',
        '26/12/2022'
    ]

    # Convert UK bank holidays to datetime objects
    uk_bank_holidays = pd.to_datetime(uk_bank_holidays, format='%d/%m/%Y')

    # Calculate the difference in business days between "Acctg Date" and "Date" columns for each row
    merged_df['Business Days Difference'] = merged_df.apply(
        lambda row: np.busday_count(row['Date'].date(), row['Acctg Date'].date(), holidays=[x.date() for x in uk_bank_holidays]),
        axis=1
    )

    # Calculate the difference in days between "Acctg Date" and "Date" columns for each row
    merged_df['Date Difference'] = (merged_df['Acctg Date'] - merged_df['Date']).dt.days

    # Display the merged and de-duplicated DataFrame
    print("\nMerged and de-duplicated DataFrame after PLN Exchange :")
    merged_df = convert_to_pln(merged_df)

    # Call the function to save files by Type
    save_files_by_type(merged_df)
    # print(merged_df)
