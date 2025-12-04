"""
Data Loader Module
------------------
This module loads the sales dataset from a CSV file.
"""

import pandas as pd

def load_data(file_path):
    """
    Load e-commerce sales data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file

    Returns:
    pd.DataFrame: Loaded sales data
    """
    df = pd.read_csv(file_path)
    return df
