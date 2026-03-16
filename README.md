# E-Commerce Product Analytics

## Project Overview

This project analyzes customer behavior on an e-commerce platform to understand purchasing patterns, product performance, and revenue trends.
The analysis focuses on identifying user actions such as product views, cart additions, and purchases in order to improve conversion rates and business decision-making.

The dataset contains millions of user interaction events collected from an online multi-category store.

---

## Objectives

* Analyze user behavior across the purchase funnel
* Identify drop-off points in the customer journey
* Determine top performing products and categories
* Analyze revenue trends over time
* Identify high-value customers

---

## Dataset

Dataset source: Kaggle

The dataset contains the following fields:

| Column        | Description                          |
| ------------- | ------------------------------------ |
| event_time    | Timestamp of user action             |
| event_type    | Type of event (view, cart, purchase) |
| product_id    | Unique product identifier            |
| category_id   | Category identifier                  |
| category_code | Product category                     |
| brand         | Product brand                        |
| price         | Product price                        |
| user_id       | Unique user identifier               |
| user_session  | Session identifier                   |

---

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* Jupyter Notebook / VS Code
* Power BI for dashboard visualization

---

## Key Analyses Performed

### Data Cleaning

* Removed duplicate records
* Converted timestamps to datetime format
* Checked and handled missing values

### Funnel Analysis

Analyzed user journey through the stages:

View → Cart → Purchase

Calculated:

* Cart conversion rate
* Purchase conversion rate
* Cart abandonment rate

### Revenue Analysis

* Total revenue generated
* Revenue trends over time
* Revenue by product and category

### Product Performance

* Top products by revenue
* Most viewed products
* Best performing categories

### Customer Analysis

* Top customers by purchase value
* Customer purchase behavior

---

## Dashboard

An interactive dashboard was created in Power BI showing:

* Total revenue
* Conversion funnel
* Revenue trend over time
* Top selling products
* Sales by category
* Customer insights

---

## Project Structure

```
ecommerce-product-analytics
│
├── data
│   └── 2019-Nov.csv
│
├── analysis.py
├── dashboard.pbix
├── visuals
└── README.md
```

---

## Key Insights

* A large percentage of users view products but do not complete purchases.
* Cart abandonment represents a major opportunity for optimization.
* A small number of products contribute significantly to overall revenue.
* Customer behavior varies across product categories and time periods.

---

## Future Improvements

* Customer segmentation using clustering
* Predictive modeling for purchase likelihood
* Recommendation system for product suggestions
* Advanced cohort analysis

---

## Author

Sunny Shekhar Singh
Data Analyst | Python | SQL | Data Visualization
