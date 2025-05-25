# Visualizing Electronics Sales Trends with Python project 

## 📌 Project Overview
The project focuses on preprocessing a sample dataset, including data cleaning, handling missing values, feature engineering, and initial visualization to identify trends and anomalies.
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


