# Pandas: Series and DataFrame
# --------------------------------
# Pandas mainly provides two important data structures:

# 1. Series      -> One-dimensional data structure
# 2. DataFrame   -> Two-dimensional data structure

# Both Series and DataFrame have a default integer index starting from 0.

import pandas as pd


# ============================================================
# 1. DATA SERIES
# ============================================================

# Create a Series
marks = pd.Series([85, 90, 78, 95])

print("Marks:")
print(marks)


# ============================================================
# 2. CUSTOM INDEXING IN SERIES
# ============================================================

marks = pd.Series(
    [85, 90, 78, 95],
    index=["a", "b", "c", "d"]
)

print("\nMarks with Custom Indexing:")
print(marks)


# ============================================================
# 3. CREATE SERIES USING A DICTIONARY
# ============================================================

# Dictionary keys become the Series index
population = {
    "Delhi": 11000,
    "Mumbai": 22000,
    "Kolkata": 33000
}

population_series = pd.Series(population)

print("\nPopulation Series:")
print(population_series)


# ============================================================
# 4. SELECT VALUES FROM A SERIES
# ============================================================

print("\nSelecting Values from Series:")

# Select a value using its index
print("Delhi Population:", population_series["Delhi"])

# Select multiple values
print("\nDelhi and Mumbai:")
print(population_series[["Delhi", "Mumbai"]])


# ============================================================
# 5. DATAFRAME
# ============================================================

# A DataFrame is a two-dimensional table-like data structure.
# It is similar to a table in Excel or a database table.

data = {
    "Name": ["Amit", "Rahul", "Neha", "Kunal", "Yogesh", "Lokesh"],
    "Age": [25, 30, 28, 23, 45, 21],
    "Salary": [50000, 65000, 70000, 45000, 55000, 61000]
}

df = pd.DataFrame(data)

print("\nEmployee DataFrame:")
print(df)


# ============================================================
# 6. SELECT COLUMNS FROM A DATAFRAME
# ============================================================

print("\nName Column:")
print(df["Name"])

print("\nName and Salary Columns:")
print(df[["Name", "Salary"]])
