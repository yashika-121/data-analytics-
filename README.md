# Visualizing Electronics Sales Trends with Python project 

## 📌 Project Overview :
This project focuses on preprocessing and visualizing a 12-month electronics sales dataset using Python. It covers data cleaning, handling missing values, feature engineering, and exploratory visualization to uncover business trends and anomalies.

Dataset: Sales data from sep2023 to sep2024 from an electronics retailer.

Business Context:

Understand sales patterns and peak seasons
Identify top-performing products and revenue drivers
Support data-driven marketing and inventory decisions

Brief background of the dataset (12 months of electronics store sales)
  Business context: understanding customer behavior, improving sales strategies
  Tools used: Python, Pandas, Matplotlib


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
| Visualize           | Saves two PNGs in `outputs/`: `monthly_revenue.png` (line chart) and `product_revenue.png` (bar chart). 

Sample Outputs
You can find the visualizations inside the outputs/ folder:

📈 Monthly Revenue – Shows seasonal peaks (e.g., holiday sales in Nov–Dec)

📊 Product Revenue – Highlights best-selling product categories



