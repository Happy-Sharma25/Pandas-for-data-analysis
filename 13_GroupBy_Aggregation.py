# ============================================================
# Pandas DataFrame - GroupBy and Aggregation
# ============================================================

import pandas as pd


# ============================================================
# 1. Create DataFrame
# ============================================================

df = pd.DataFrame({
    "Employee": ["Amit", "Priya", "Rahul", "Neha", "Rohan", "Anjali"],
    "Department": ["HR", "HR", "IT", "IT", "Sales", "Sales"],
    "City": ["Delhi", "Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Salary": [35000, 50000, 45000, 55000, 40000, 42000]
})

print(df)


# ============================================================
# 2. GroupBy One Column
# ============================================================

# groupby() divides the data into groups based on a column.

# SQL equivalent:
# SELECT Department, AVG(Salary)
# FROM Employees
# GROUP BY Department;

# groupby() by itself returns a GroupBy object.
# It becomes useful when combined with an aggregation function.

print(df.groupby("Department"))


# Groups:
# HR    -> Amit, Priya
# IT    -> Rahul, Neha
# Sales -> Rohan, Anjali


# ============================================================
# 3. SUM
# ============================================================

# Calculate total salary for each department.

result = df.groupby("Department")["Salary"].sum()

print(result)


# ============================================================
# 4. MEAN
# ============================================================

# Calculate average salary for each department.

result = df.groupby("Department")["Salary"].mean()

print(result)


# ============================================================
# 5. COUNT
# ============================================================

# count() counts non-missing values in the selected column.

result = df.groupby("Department")["Salary"].count()

print(result)


# ============================================================
# 6. SIZE
# ============================================================

# size() counts the total number of rows in each group.
# It also includes rows containing missing values.

result = df.groupby("Department").size()

print(result)


# ============================================================
# 7. MAX
# ============================================================

# Find the highest salary in each department.

result = df.groupby("Department")["Salary"].max()

print(result)


# ============================================================
# 8. MIN
# ============================================================

# Find the lowest salary in each department.

result = df.groupby("Department")["Salary"].min()

print(result)


# ============================================================
# 9. Multiple Aggregations
# ============================================================

# Apply multiple aggregation functions at the same time.

result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "count", "max", "min"]
)

print(result)


# ============================================================
# 10. GroupBy Multiple Columns
# ============================================================

# Group data by Department and City,
# then calculate total salary for each combination.

result = df.groupby(["Department", "City"])["Salary"].sum()

print(result)


# ============================================================
# Summary
# ============================================================

# groupby() -> Divide data into groups
# sum()     -> Calculate total
# mean()    -> Calculate average
# count()   -> Count non-missing values
# size()    -> Count rows, including missing values
# max()     -> Find maximum value
# min()     -> Find minimum value
# agg()     -> Apply multiple aggregation functions
