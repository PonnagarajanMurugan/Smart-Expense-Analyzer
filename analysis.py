import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Total expense
total_expense = df["Amount"].sum()
print("Total Expense:", total_expense)

# Category-wise expense
print("\nCategory-wise Expense:")
print(df.groupby("Category")["Amount"].sum())

# Show available categories
categories = sorted(df["Category"].unique())

print("\nAvailable Categories:")
for cat in categories:
    print("-", cat)

# User input
category = input("\nEnter category to filter (or type ALL): ").strip().lower()

# Filter data
if category == "all":
    filtered_data = df.copy()
else:
    filtered_data = df[
        df["Category"].str.strip().str.lower() == category
    ]

# Check if data exists
if filtered_data.empty:
    print("\nNo records found for this category.")
    exit()

# Show filtered data
print("\nFiltered Data:")
print(filtered_data)

# Date conversion
filtered_data["Date"] = pd.to_datetime(
    filtered_data["Date"],
    dayfirst=True
)

# Analysis
category_expense = filtered_data.groupby("Category")["Amount"].sum()
daily_expense = filtered_data.groupby("Date")["Amount"].sum()

# Save summary
category_expense.to_csv("summary.csv")

# Insight
max_category = category_expense.idxmax()
max_amount = category_expense.max()

print(f"\nHighest Spending Category: {max_category} ({max_amount})")

# Dashboard
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Bar Chart
category_expense.plot(kind="bar", ax=axes[0])
axes[0].set_title("Category Expense")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Amount")

# Pie Chart
category_expense.plot(kind="pie", autopct="%1.1f%%", ax=axes[1])
axes[1].set_title("Distribution")
axes[1].set_ylabel("")

# Line Chart
daily_expense.plot(kind="line", marker="o", ax=axes[2])
axes[2].set_title("Daily Trend")
axes[2].set_xlabel("Date")
axes[2].set_ylabel("Amount")

plt.tight_layout()
plt.show()