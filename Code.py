import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r'C:\Users\admin\Desktop\Data\2019-Nov.csv')

# Convert event_time to datetime
df['event_time'] = pd.to_datetime(df['event_time'])

# Basic dataset information
print("Dataset Shape:")
print(df.shape)

print("\nColumn Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 rows:")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# -----------------------------
# Funnel Analysis
# -----------------------------
views = df[df['event_type'] == 'view']['user_id'].nunique()
carts = df[df['event_type'] == 'cart']['user_id'].nunique()
purchases = df[df['event_type'] == 'purchase']['user_id'].nunique()

print("\nFunnel Analysis")
print("Views:", views)
print("Carts:", carts)
print("Purchases:", purchases)

cart_rate = carts / views
purchase_rate = purchases / carts

print("\nCart Conversion Rate:", cart_rate)
print("Purchase Conversion Rate:", purchase_rate)

# -----------------------------
# Revenue Analysis
# -----------------------------
purchase_df = df[df['event_type'] == 'purchase']

total_revenue = purchase_df['price'].sum()

print("\nTotal Revenue:", total_revenue)

# -----------------------------
# Top Products
# -----------------------------
top_products = purchase_df.groupby('product_id')['price'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Revenue:")
print(top_products)

# -----------------------------
# Revenue Trend
# -----------------------------
daily_revenue = purchase_df.groupby(purchase_df['event_time'].dt.date)['price'].sum()

plt.figure()
daily_revenue.plot()
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# Top Customers
# -----------------------------
top_customers = purchase_df.groupby('user_id')['price'].sum().sort_values(ascending=False).head(10)

print("\nTop Customers by Revenue:")
print(top_customers)