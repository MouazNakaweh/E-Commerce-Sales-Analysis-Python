"""
Analysis Module
---------------
This module contains functions to perform:
- Sales summary
- Top products and categories
- State-wise and monthly sales trends
- Profitable sub-categories
"""

import pandas as pd

def total_sales(df):
    """Calculate total sales"""
    return df['Sales'].sum()

def average_sales(df):
    """Calculate average sales per order"""
    return df['Sales'].mean()

def top_selling_products(df, top_n=10):
    """Return top-selling products"""
    return df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(top_n)

def top_categories(df):
    """Return top-selling categories and sub-categories"""
    categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    sub_categories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
    return categories, sub_categories

def monthly_sales(df):
    """Return monthly sales summary"""
    df['Month'] = df['Order Date'].dt.month_name()
    return df.groupby('Month')['Sales'].sum().sort_index()
