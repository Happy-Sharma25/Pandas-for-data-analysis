# ============================================================
# Pandas DataFrame - Sorting Data
# ============================================================

import numpy as np
import pandas as pd


# ============================================================
# 1. CREATE A DATAFRAME
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Rohan"],
    "Age": [25, 30, 28, 26, 35],
    "Department": ["HR", "Sales", "IT", "HR", "IT"],
    "Salary": [35000, 50000, 45000, 38000, 60000]
})

print("Original DataFrame:")
print(df)


# ============================================================
# 2. SORT BY A SINGLE COLUMN
# ============================================================

# Sort Salary in ascending order.
# Ascending order is the default.
print("\nSalary - Ascending Order:")
print(df.sort_values("Salary"))


# Sort Salary in descending order.
print("\nSalary - Descending Order:")
print(df.sort_values("Salary", ascending=False))


# ============================================================
# 3. SORT BY MULTIPLE COLUMNS
# ============================================================

# First sort Department alphabetically (A-Z).
# Then sort Salary in descending order within each department.

print("\nDepartment (A-Z) and Salary (Highest First):")
print(
    df.sort_values(
        by=["Department", "Salary"],
        ascending=[True, False]
    )
)


# ============================================================
# 4. SORT BY INDEX
# ============================================================

# Sort the DataFrame by index in ascending order.
print("\nSorted by Index - Ascending:")
print(df.sort_index())


# Sort the DataFrame by index in descending order.
print("\nSorted by Index - Descending:")
print(df.sort_index(ascending=False))


# ============================================================
# 5. RESET INDEX WHILE SORTING
# ============================================================

# By default, sort_values() keeps the original index.

print("\nSalary Sorted - Original Index:")
print(df.sort_values("Salary"))


# ignore_index=True creates a new sequential index.
print("\nSalary Sorted - New Index:")
print(
    df.sort_values(
        "Salary",
        ignore_index=True
    )
)


# ============================================================
# 6. SAVE SORTED DATA
# ============================================================

# Store the sorted DataFrame in a new variable.
sorted_data = df.sort_values("Department")

print("\nData Sorted by Department:")
print(sorted_data)


# ============================================================
# 7. MODIFY THE ORIGINAL DATAFRAME
# ============================================================

# inplace=True changes the original DataFrame.

# Example:
df.sort_values(
    "Age",
    ascending=True,
    inplace=True,
    ignore_index=True
)

print(df)


# ============================================================
# 8. SORTING DATES
# ============================================================

date = pd.DataFrame({
    "Dates": [
        "2025-02-10",
        "2025-01-15",
        "2025-03-05"
    ]
})

print("\nOriginal Dates:")
print(date)


# Convert the column from string to datetime.
date["Dates"] = pd.to_datetime(date["Dates"])

print("\nDates Sorted:")
print(date.sort_values("Dates"))


# ============================================================
# 9. SORTING WITH MISSING VALUES
# ============================================================

missing = pd.DataFrame({
    "Salary": [35000, np.nan, 50000, 25000]
})

print("\nData with Missing Value:")
print(missing)


# By default, missing values are placed at the end.
print("\nSorted Data:")
print(missing.sort_values("Salary"))


# ============================================================
# 10. LARGEST VALUES
# ============================================================

# nlargest() returns the rows with the largest values.

print("\nTop 3 Highest Salaries:")
print(df.nlargest(3, "Salary"))


# ============================================================
# 11. SMALLEST VALUES
# ============================================================

# nsmallest() returns the rows with the smallest values.

print("\nTop 3 Lowest Salaries:")
print(df.nsmallest(3, "Salary"))


# ============================================================
# Summary
# ============================================================

# sort_values()              -> Sort by column values
# sort_index()               -> Sort by index
# ascending=False            -> Descending order
# ignore_index=True          -> Create a new sequential index
# inplace=True               -> Modify the original DataFrame
# pd.to_datetime()           -> Convert values to datetime
# nlargest()                 -> Get largest values
# nsmallest()                -> Get smallest values

# ============================================================

