import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

RAW_PATH = r"C:\Users\admin\Downloads\Electronicsales_Sep2023-Sep2024.csv"
CLEAN_PATH = os.path.join('data', 'processed', 'electronics_sales_cleaned.csv')
OUTPUT_DIR = 'outputs'

def load_data(path: str) -> pd.DataFrame:
    """Load CSV and parse dates."""
    df = pd.read_csv(path, parse_dates=['Purchase Date'])
    df.columns = df.columns.str.strip()
    return df

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates, handle non-positive values, and compute revenue."""
    df = df.drop_duplicates()
    df = df[(df['Quantity'] > 0) & (df['Unit Price'] > 0)]
    df['Revenue'] = df['Quantity'] * df['Unit Price']
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Add Month, Quarter, and Year columns for analysis."""
    df['Month'] = df['Purchase Date'].dt.month
    df['MonthName'] = df['Purchase Date'].dt.strftime('%b')
    df['Quarter'] = df['Purchase Date'].dt.quarter
    df['Year'] = df['Purchase Date'].dt.year
    return df

def save_clean_data(df: pd.DataFrame, path: str) -> None:
    """Saves the cleaned DataFrame to a CSV file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)



def plot_monthly_revenue(df: pd.DataFrame) -> None:
    """Plots total revenue per month (Line Chart)."""
    
    monthly = df.groupby('Month')['Revenue'].sum().sort_index()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    monthly.plot(kind='line', marker='o', color='royalblue', linewidth=2, markersize=8)
    plt.title('Total Monthly Revenue Trend (Sep 2023 - Sep 2024)', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Revenue', fontsize=12)
    plt.xticks(ticks=monthly.index, labels=df.sort_values('Month')['MonthName'].unique(), rotation=45)
    formatter = FuncFormatter(lambda x, pos: f'${x/1000:.0f}K')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'monthly_revenue.png'))
    plt.close()


def plot_product_revenue(df: pd.DataFrame) -> None:
    """Plots total revenue by product type (Bar Chart)."""

    product_rev = df.groupby('Product Type')['Revenue'].sum().sort_values(ascending=False)
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    product_rev.plot(kind='bar', color='skyblue')
    plt.title('Total Revenue by Product Type', fontsize=16)
    plt.xlabel('Product Type', fontsize=12)
    plt.ylabel('Total Revenue', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    formatter = FuncFormatter(lambda x, pos: f'${x/1000:.0f}K')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'product_revenue.png'))
    plt.close()



def plot_monthly_quantity(df: pd.DataFrame) -> None:
    """
    Plots the total quantity of items sold each month. (Line Chart)

    Interpretation and Storytelling:
    This chart complements the monthly revenue chart. By tracking sales volume (quantity),
    we can see if revenue trends are driven by selling more items or by selling more
    expensive items. If the quantity trend mirrors the revenue trend, it indicates
    consistent purchasing behavior. If they diverge, it suggests a shift in the average
    price of items sold during certain months (e.g., high-ticket items during holidays).
    """
    monthly_qty = df.groupby('Month')['Quantity'].sum().sort_index()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    monthly_qty.plot(kind='line', marker='s', color='seagreen', linewidth=2, markersize=8)
    plt.title('Total Items Sold Per Month', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Quantity Sold', fontsize=12)
    plt.xticks(ticks=monthly_qty.index, labels=df.sort_values('Month')['MonthName'].unique(), rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'monthly_quantity.png'))
    plt.close()

def plot_quarterly_revenue_pie(df: pd.DataFrame) -> None:
    """
    Shows the proportion of total revenue contributed by each quarter. (Pie Chart)

    Interpretation and Storytelling:
    This pie chart provides a high-level overview of the business cycle, showing which
    quarters are most critical to annual revenue. A large slice for Q4, for instance,
    would emphasize the importance of the holiday season. This visualization is great
    for executive summaries to quickly show parts-of-a-whole contribution.
    """
    quarterly_rev = df.groupby('Quarter')['Revenue'].sum()
    
    explode_values = [0.1 if q == quarterly_rev.idxmax() else 0 for q in quarterly_rev.index]

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(8, 8))
    plt.pie(quarterly_rev, labels=[f'Q{q}' for q in quarterly_rev.index],
            autopct='%1.1f%%', startangle=140,
            explode=explode_values, shadow=True)
    plt.title('Revenue Contribution by Quarter', fontsize=16)
    plt.ylabel('') 
    plt.savefig(os.path.join(OUTPUT_DIR, 'quarterly_revenue_pie.png'))
    plt.close()

def plot_price_vs_quantity_scatter(df: pd.DataFrame) -> None:
    """
    Examines the relationship between unit price and quantity per order. (Scatter Chart)

    Interpretation and Storytelling:
    This scatter plot investigates purchasing behavior: do customers buy items in larger
    quantities when the unit price is low? The concentration of points in the bottom-left

    suggests most transactions involve low-quantity, low-priced items. A lack of points in
    the top-right is expected (few people buy many expensive items at once). This can
    help identify typical basket sizes and inform pricing or bundling strategies.
    """
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    sample_df = df.sample(n=min(len(df), 1000), random_state=1)
    plt.scatter(sample_df['Unit Price'], sample_df['Quantity'], alpha=0.5, color='darkorange')
    plt.title('Unit Price vs. Order Quantity', fontsize=16)
    plt.xlabel('Unit Price ($)', fontsize=12)
    plt.ylabel('Quantity in Order', fontsize=12)
    plt.xscale('log') 
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'price_vs_quantity_scatter.png'))
    plt.close()



def main():
    
    if not os.path.exists(RAW_PATH):
        print(f"Warning: File not found at {RAW_PATH}. Creating dummy data for demonstration.")
        dummy_data = {
            'Purchase Date': pd.to_datetime(['2023-09-15', '2023-11-20', '2023-11-22', '2024-02-10', '2024-04-05', '2024-07-18']),
            'Product Type': ['Laptop', 'Smartphone', 'Headphones', 'Laptop', 'Smart Watch', 'Smartphone'],
            'Unit Price': [1200, 800, 150, 1350, 250, 900],
            'Quantity': [1, 2, 3, 1, 2, 1]
        }
        df = pd.DataFrame(dummy_data)
    else:
        df = load_data(RAW_PATH)

    
    df = basic_cleaning(df)
    df = feature_engineering(df)
    os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
    save_clean_data(df, CLEAN_PATH)

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plot_monthly_revenue(df)
    plot_product_revenue(df)
    plot_monthly_quantity(df)         
    plot_quarterly_revenue_pie(df)    
    plot_price_vs_quantity_scatter(df)

    print(f" Preprocessing & visualization complete. 5 charts saved to the '{OUTPUT_DIR}' directory.")

if __name__ == '__main__':
    main()
