import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = "data/raw/Ecommerce_Growth_Customer_Intelligence_5000.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Raw_Data"
)

# Convert numeric columns
for column in ["Revenue", "Profit"]:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)

# ==============================
# MONTHLY ANALYSIS
# ==============================

monthly = (
    df.groupby(
        df["Order_Date"].dt.to_period("M")
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

# Convert period to text
monthly["Order_Date"] = monthly["Order_Date"].astype(str)

# Display results
print("===== MONTHLY PERFORMANCE =====")

print(
    monthly.round(0).to_string(index=False)
)

# ==============================
# MONTHLY REVENUE & PROFIT CHART
# ==============================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly["Order_Date"],
    monthly["Revenue"],
    marker="o",
    label="Revenue"
)

plt.plot(
    monthly["Order_Date"],
    monthly["Profit"],
    marker="o",
    label="Profit"
)

plt.title(
    "Monthly Revenue and Profit Trend"
)

plt.xlabel("Month")

plt.ylabel("Amount (₹)")

plt.xticks(
    rotation=60
)

plt.legend()

plt.tight_layout()

# Save chart
plt.savefig(
    "dashboard/monthly_revenue_profit_python.png",
    dpi=300
)

plt.show()