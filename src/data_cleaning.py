"""
Data Cleaning Module
-------------------
This module handles data cleaning tasks:
- Remove duplicates
- Handle missing values
- Convert data types
"""

def clean_data(df):
    """
    Clean the sales data

    Parameters:
    df (pd.DataFrame): Raw sales data

    Returns:
    pd.DataFrame: Cleaned data
    """
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values (example: fill missing 'State' with 'Unknown')
    df['State'] = df['State'].fillna('Unknown')

    # Convert 'Order Date', 'Ship Date' to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Make new columns for the quarter and month
    df["YearQuarter"] = df["Order Date"].dt.to_period('Q')
    df["YearMonth"] = df["Order Date"].dt.to_period('M')

    return df
