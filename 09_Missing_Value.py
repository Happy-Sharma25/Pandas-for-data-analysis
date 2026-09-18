# ============================================================
# Pandas DataFrame - Handling Missing Values
# ============================================================

import numpy as np
import pandas as pd


# ============================================================
# 1. CREATE A DATAFRAME WITH MISSING VALUES
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Priya", np.nan, "Neha"],
    "Age": [25, np.nan, 28, 26],
    "Salary": [35000, 50000, np.nan, 38000]
})

print("Original DataFrame:")
print(df)


# ============================================================
# 2. CHECK FOR MISSING VALUES
# ============================================================

# isnull(): Returns True where a value is missing.
print("\nMissing Value Check using isnull():")
print(df.isnull())


# notnull(): Returns True where a value is NOT missing.
print("\nNon-Missing Value Check using notnull():")
print(df.notnull())


# isna(): Same as isnull().
print("\nMissing Value Check using isna():")
print(df.isna())


# ============================================================
# 3. COUNT MISSING VALUES
# ============================================================

# Count missing values in each column.
print("\nMissing Values in Each Column:")
print(df.isnull().sum())


# Count total missing values in the entire DataFrame.
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# Count missing values in each row.
print("\nMissing Values in Each Row:")
print(df.isnull().sum(axis=1))


# ============================================================
# 4. SUM OF DATAFRAME VALUES
# ============================================================

# sum() performs column-wise addition by default.
# Missing values are ignored by default.

print("\nColumn-wise Sum:")
print(df.sum(numeric_only=True))

# Age:
# 25 + 28 + 26 = 79

# Salary:
# 35000 + 50000 + 38000 = 123000


# ============================================================
# 5. REPLACE MISSING VALUES WITH A FIXED VALUE
# ============================================================

# fillna(0) replaces every missing value with 0.

print("\nMissing Values Replaced with 0:")
print(df.fillna(0))


# ============================================================
# 6. REPLACE MISSING VALUES WITH COLUMN MEAN
# ============================================================

# Calculate the mean of numeric columns.
numeric_mean = df.mean(numeric_only=True).round(2)

print("\nMean of Numeric Columns:")
print(numeric_mean)


# Replace missing numeric values with their respective
# column mean.
df_filled = df.fillna(numeric_mean)

print("\nMissing Values Replaced with Column Mean:")
print(df_filled)


# ============================================================
# Summary
# ============================================================

# isnull() / isna()       -> Check for missing values
# notnull()               -> Check for non-missing values
# isnull().sum()          -> Count missing values by column
# isnull().sum().sum()    -> Count total missing values
# axis=1                  -> Perform operation row-wise
# fillna(0)               -> Replace missing values with 0
# fillna(mean)            -> Replace missing values with mean

# ============================================================
