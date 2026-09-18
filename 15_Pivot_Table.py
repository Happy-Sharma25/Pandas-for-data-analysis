# ============================================================
# Pandas - Pivot Table
# ============================================================

import pandas as pd


# ============================================================
# 1. Create DataFrame
# ============================================================

df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Sales", "Sales"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai"],
    "Salary": [35000, 50000, 45000, 55000, 40000, 42000]
})

print(df)


# ============================================================
# 2. Basic Pivot Table
# ============================================================

# pivot_table() calculates the mean by default.

# HR average:
# (35000 + 50000) / 2 = 42500

result = pd.pivot_table(
    df,
    values="Salary",
    index="Department"
)

print(result)


# ============================================================
# 3. Sum Instead of Mean
# ============================================================

# aggfunc="sum" calculates the total salary
# for each department.

result = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="sum"
)

print(result)


# ============================================================
# 4. Multiple Aggregation Functions
# ============================================================

result = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc=["sum", "mean", "count", "max", "min"]
)

print(result)


# ============================================================
# 5. Add Columns to the Pivot Table
# ============================================================

# Department becomes rows.
# City becomes columns.
# Salary is aggregated using sum.

result = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="sum"
)

print(result)


# ============================================================
# 6. Multiple Index Columns
# ============================================================

# Group by both Department and City.

result = pd.pivot_table(
    df,
    values="Salary",
    index=["Department", "City"],
    aggfunc="sum"
)

print(result)


# ============================================================
# 7. Fill Missing Values
# ============================================================

# fill_value=0 replaces missing values with 0.

result = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="sum",
    fill_value=0
)

print(result)


# ============================================================
# 8. Add Row and Column Totals
# ============================================================

# margins=True adds an "All" row and column
# containing the totals.

result = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="sum",
    margins=True
)

print(result)


# ============================================================
# 9. Pivot
# ============================================================

# pivot() reshapes data without performing aggregation.

# Each Department + City combination must have
# exactly one corresponding Salary value.

result = df.pivot(
    index="Department",
    columns="City",
    values="Salary"
)

print(result)


# ============================================================
# 10. GroupBy and Pivot Table
# ============================================================

# Both can produce the same departmental salary total.

result1 = df.groupby("Department")["Salary"].sum()

print(result1)

result2 = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="sum"
)

print(result2)


# ============================================================
# Summary
# ============================================================

# pivot_table() -> Creates a summary table with aggregation

# values       -> Column to calculate
# index        -> Row grouping
# columns      -> Column grouping
# aggfunc      -> Aggregation function
# fill_value   -> Replace missing values
# margins=True -> Add totals

# pivot()      -> Reshapes data without aggregation
