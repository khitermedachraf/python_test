import os

import pandas as pd
# We need also to install the 'openpyxl' module which is required for reading Excel files:  pip install openpyxl


def task_2():
    # Load the Excel file into a DataFrame
    df = pd.read_excel("interval_data.xlsx")

    # Melt the DataFrame to transform Hour columns into rows
    melted_df = pd.melt(df, id_vars=["MPAN", "Date"], var_name="Hour", value_name="Value")

    # Extract the Hour values from the Hour column
    melted_df["Hour"] = melted_df["Hour"].str.split(":").str[0]

    # Convert 'Date' column to datetime format
    melted_df['Date'] = pd.to_datetime(melted_df['Date'])

    # Group by 'MPAN' and week of the year
    grouped = melted_df.groupby(['MPAN', melted_df['Date'].dt.isocalendar().week])

    # Calculate mean, max, and min values for each group
    result = grouped.agg({'Value': ['mean', 'max', 'min']})

    # Rename the columns for clarity
    result.columns = ['Mean', 'Max', 'Min']

    # Reset index to make 'MPAN' and 'Date' as columns instead of index
    result.reset_index(inplace=True)

    # Create a folder named 'results_task2' if it doesn't exist
    if not os.path.exists('results_task2'):
        os.makedirs('results_task2')

    # Loop through each MPAN and save to separate files in the results_task2 folder
    for mpan, df in result.groupby(level=0):
        file_name = f"results_task2/MPAN_{mpan}.xlsx"
        df.to_excel(file_name)

    # Display the resulting DataFrame
    print(result)



