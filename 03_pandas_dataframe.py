# ============================================================
# Pandas DataFrame
# ============================================================

# A DataFrame is a two-dimensional, table-like data structure in Pandas. It consists of rows and columns and is similar
# to a table in Excel or a database.

# ============================================================

import pandas as pd


# ============================================================
# 1. CREATE A DATAFRAME
# ============================================================

data = {
    "Name": ["Amit", "Rahul", "Neha", "Kunal", "Yogesh", "Lokesh"],
    "Age": [25, 30, 28, 23, 45, 21],
    "Salary": [50000, 65000, 70000, 45000, 55000, 61000]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)


# ============================================================
# 2. DATAFRAME METHODS
# ============================================================

# head(): Returns the first 5 rows by default
print("\nFirst 5 Rows:")
print(df.head())


# tail(): Returns the last 5 rows by default
print("\nLast 5 Rows:")
print(df.tail())


# info(): Displays information about the DataFrame
print("\nDataFrame Information:")
df.info()

# Typical information displayed by info():

# - Number of rows
# - Column names
# - Number of non-null values
# - Data types
# - Memory usage


# describe(): Returns statistical summary of numeric columns
print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# 3. DATAFRAME ATTRIBUTES
# ============================================================

# shape: Returns (number of rows, number of columns)
print("\nDataFrame Shape:")
print(df.shape)


# columns: Returns all column names
print("\nDataFrame Columns:")
print(df.columns)


# index: Returns row labels
print("\nDataFrame Index:")
print(df.index)


# dtypes: Returns the data type of each column
print("\nData Types of Columns:")
print(df.dtypes)


# size: Returns the total number of elements
# Formula: rows × columns
print("\nDataFrame Size:")
print(df.size)


# ndim: Returns the number of dimensions
# DataFrame = 2 dimensions
print("\nNumber of Dimensions:")
print(df.ndim)


# ============================================================
# Series vs DataFrame
# ============================================================

# Series    -> 1-dimensional
# DataFrame -> 2-dimensional

# ============================================================
