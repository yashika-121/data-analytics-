"""
preprocessing_sales.py
----------------------
Clean, transform, and visualize a 12‑month electronics sales dataset.

Expected input:
    data/raw/electronics_sales_2023.csv

Outputs:
    data/processed/electronics_sales_cleaned.csv
    outputs/monthly_revenue.png
    outputs/product_revenue.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

RAW_PATH = r"C:\Users\admin\Downloads\Electronicsales_Sep2023-Sep2024.csv"
CLEAN_PATH = os.path.join('data', 'processed', 'electronics_sales_cleaned.csv')
OUTPUT_DIR = os.path.join('outputs')

def load_data(path: str) -> pd.DataFrame:
    """Load CSV and parse dates."""
    df = pd.read_csv(path, parse_dates=['Purchase Date'])
    df.columns = df.columns.str.strip()  # Clean column names
    return df

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates, handle non‑positive values."""
    df = df.drop_duplicates()

    # Filter non-positive values
    df = df[(df['Quantity'] > 0) & (df['Unit Price'] > 0)]

    # Compute Revenue
    df['Revenue'] = df['Quantity'] * df['Unit Price']

    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Add Month, Quarter, and Year columns."""
    df['Month'] = df['Purchase Date'].dt.month
    df['MonthName'] = df['Purchase Date'].dt.strftime('%b')
    df['Quarter'] = df['Purchase Date'].dt.quarter
    df['Year'] = df['Purchase Date'].dt.year
    return df

def save_clean_data(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

def plot_monthly_revenue(df: pd.DataFrame) -> None:
    monthly = df.groupby('Month')['Revenue'].sum()
    plt.figure(figsize=(10, 5))
    monthly.plot(kind='line', marker='o')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(ticks=range(1, 13))
    plt.grid(True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.savefig(os.path.join(OUTPUT_DIR, 'monthly_revenue.png'))
    plt.close()

def plot_product_revenue(df: pd.DataFrame) -> None:
    product_rev = df.groupby('Product Type')['Revenue'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    product_rev.plot(kind='bar')
    plt.title('Total Revenue by Product')
    plt.xlabel('Product Type')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.savefig(os.path.join(OUTPUT_DIR, 'product_revenue.png'))
    plt.close()

def main():
    if not os.path.exists(RAW_PATH):
        raise FileNotFoundError(f'Input file not found at {RAW_PATH}.')
    
    df = load_data(RAW_PATH)
    df = basic_cleaning(df)
    df = feature_engineering(df)
    save_clean_data(df, CLEAN_PATH)

    # Visualizations
    plot_monthly_revenue(df)
    plot_product_revenue(df)

    print('Preprocessing & visualization complete. Outputs saved to:', OUTPUT_DIR)

if __name__ == '__main__':
    main()
