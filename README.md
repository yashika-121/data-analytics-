# Visualizing Electronics Sales Trends with Python project 

## 📌 Project Overview ( what is the project is about?)
This project focuses on analyzing and visualizing 12 months of electronics sales data (from September 2023 to September 2024) to uncover trends, peak seasons, and top-performing products. It involves data preprocessing, feature engineering, and exploratory data visualization to support strategic business decisions in marketing and inventory planning.



Dataset: Sales data from sep2023 to sep2024 from an electronics retailer.
Brief background of the dataset (12 months of electronics store sales)
Business context: understanding customer behavior, improving sales strategies

  
Tools used: 
Python, Pandas, Matplotlib


##_project structure
├── data
│   ├── raw
│   │   └── electronics_sales_2023.csv   
│   └── processed                      
├── outputs                            
└── src
    └── preprocessing_sales.py           

## what it does?

| Step                | Action              
| Load                | Reads `electronics_sales_2023.csv`, parses `Date`.                                                      
| Clean               | Drops duplicates, ensures positive `Quantity` and `Price`, recalculates `Revenue`.                      
| Feature engineering | Adds `Month`, `MonthName`, `Quarter`, `Year`.                                                           
| Save                | Writes cleaned data to `data/processed/electronics_sales_cleaned.csv`.                                  
| Visualize           | Saves five PNGs in `outputs/`.

 What Do the Charts Shows ?
 
1) Monthly Revenue (monthly_revenue.png)
    Line chart showing monthly revenue trends.
    Reveals seasonal peaks, such as high sales in November–December.

2)  Product Revenue (product_revenue.png)
    Bar chart showing total revenue by product category.
   Highlights best-selling product categories.

3) Monthly Quantity Sold (plot_monthly_quantity.png)
   Bar chart showing the total quantity of items sold each month.
   Useful for identifying volume-driven months, independent of revenue.

4) Quarterly Revenue Share (plot_quarterly_revenue_pie.png)
   Pie chart illustrating revenue distribution across quarters (Q1–Q4).
   Helps understand quarterly performance, budget planning, and seasonal focus.

5) Price vs Quantity Scatter Plot (plot_price_vs_quantity_scatter.png)
   Scatter plot showing the relationship between product price and quantity sold.
   Useful for identifying price sensitivity and potential demand trends.
   
 
