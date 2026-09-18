# ============================================================
# Pandas Data Series
# ============================================================

# A Series is a one-dimensional labeled data structure in Pandas.
# Each value has an index. By default, the index starts from 0.

# ============================================================

import numpy as np
import pandas as pd


# ============================================================
# 1. CREATE A SERIES
# ============================================================

marks = pd.Series([85, 90, 78, 95])

print("Marks:")
print(marks)


# ============================================================
# 2. CUSTOM INDEXING
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

# Dictionary keys become the index labels of the Series.

population = {
    "Delhi": 11000,
    "Mumbai": 22000,
    "Kolkata": 33000
}

ds = pd.Series(population)

print("\nPopulation Series:")
print(ds)


# ============================================================
# 4. SELECT VALUES FROM A SERIES
# ============================================================

# Select a value by label
print("\nValue selected by label:")
print(ds["Delhi"])

# Select a value by position
print("\nValue selected by position:")
print(ds.iloc[0])


# ============================================================
# 5. SERIES ATTRIBUTES
# ============================================================

# index: Returns the index labels
print("\nSeries Index:")
print(ds.index)

# values: Returns only the values
print("\nSeries Values:")
print(ds.values)


# dtype: Returns the data type of the values

integer = pd.Series([1, 2, 3, 4, 5])
print("\nInteger Series Data Type:")
print(integer.dtype)

float_values = pd.Series([1.6, 3.5, 8.5, 6.4])
print("\nFloat Series Data Type:")
print(float_values.dtype)

alphabet = pd.Series(["A", "B", "C", "D"])
print("\nString Series Data Type:")
print(alphabet.dtype)

mixed = pd.Series([1, "A", 2.3])
print("\nMixed Series Data Type:")
print(mixed.dtype)


# size: Returns the total number of elements
print("\nSeries Size:")
print(ds.size)

# shape: Returns the dimensions of the Series
print("\nSeries Shape:")
print(ds.shape)

# ndim: Returns the number of dimensions
check = pd.Series([[1, 2, 3], [4, 5, 6]])

print("\nNumber of Dimensions:")
print(check.ndim)

# name: Returns or assigns the name of a Series
ds.name = "City Population"

print("\nSeries Name:")
print(ds.name)


# ============================================================
# 6. SERIES FUNCTIONS
# ============================================================

ds = pd.Series(
    [32000, 22000, 11000, 25000, 18000],
    index=["Delhi", "Mumbai", "Kolkata", "Chennai", "Pune"],
    name="Population"
)

print("\nPopulation Series:")
print(ds)


# head(): Returns the first 5 values by default
print("\nFirst 5 Values:")
print(ds.head())

# Return the first 2 values
print("\nFirst 2 Values:")
print(ds.head(2))


# tail(): Returns the last 5 values by default
print("\nLast 5 Values:")
print(ds.tail())

# Return the last 2 values
print("\nLast 2 Values:")
print(ds.tail(2))


# describe(): Returns statistical summary
print("\nStatistical Summary:")
print(ds.describe().round(2))


# Common Series functions:
# sum()           -> Returns the total
# min()           -> Returns the minimum value
# max()           -> Returns the maximum value
# mean()          -> Returns the average
# std()           -> Returns the standard deviation
# var()           -> Returns the variance
# unique()        -> Returns unique values
# nunique()       -> Returns the number of unique values
# sort_values()   -> Sorts values
# sort_index()    -> Sorts by index labels
# value_counts()  -> Counts occurrences of each value


# Sort values in ascending order
print("\nSorted Values:")
print(ds.sort_values())

# Sort values in descending order
print("\nSorted Values in Descending Order:")
print(ds.sort_values(ascending=False))

# Sort by index
print("\nSorted by Index:")
print(ds.sort_index())


# ============================================================
# 7. FILTERING A SERIES
# ============================================================

# Filtering means selecting values that satisfy a condition.

ds = pd.Series(
    [32000, 22000, 11000, 25000, 18000],
    index=["Delhi", "Mumbai", "Kolkata", "Chennai", "Pune"]
)

print("\nPopulation Data:")
print(ds)


# Greater than
print("\nPopulation Greater Than 20000:")
print(ds[ds > 20000])


# Less than
print("\nPopulation Less Than 20000:")
print(ds[ds < 20000])


# Greater than or equal to
print("\nPopulation Greater Than or Equal to 20000:")
print(ds[ds >= 20000])


# Less than or equal to
print("\nPopulation Less Than or Equal to 20000:")
print(ds[ds <= 20000])


# Equal to
print("\nPopulation Equal to 18000:")
print(ds[ds == 18000])


# Not equal to
print("\nPopulation Not Equal to 18000:")
print(ds[ds != 18000])


# Multiple conditions using AND
print("\nPopulation Between 20000 and 30000:")
print(ds[(ds > 20000) & (ds < 30000)])


# Multiple conditions using OR
print("\nPopulation Greater Than 30000 or Less Than 15000:")
print(ds[(ds > 30000) | (ds < 15000)])


# NOT condition
print("\nPopulation NOT Greater Than 20000:")
print(ds[~(ds > 20000)])


# ============================================================
# 8. FILTERING BY INDEX
# ============================================================

# Filter using a single index label
print("\nDelhi Population:")
print(ds[ds.index == "Delhi"])


# Filter using multiple index labels
print("\nDelhi and Pune Population:")
print(ds[ds.index.isin(["Delhi", "Pune"])])


# ============================================================
# 9. FILTERING STRING VALUES
# ============================================================

fruits = pd.Series(
    ["Apple", "Banana", "Apple", "Orange", "Mango"]
)

print("\nApple Values:")
print(fruits[fruits == "Apple"])


# ============================================================
# 10. USING isin()
# ============================================================

marks = pd.Series([1, 2, 3, 3, 4])

print("\nValues 3 and 4:")
print(marks[marks.isin([3, 4])])


# ============================================================
# 11. MISSING VALUES
# ============================================================

marks = pd.Series([10, np.nan, 30, np.nan, 50])

# isna(): Returns True for missing values
print("\nMissing Value Check:")
print(marks.isna())

# Select only missing values
print("\nMissing Values:")
print(marks[marks.isna()])


# notna(): Returns True for non-missing values
print("\nNon-Missing Values:")
print(marks[marks.notna()])


# fillna(): Replaces missing values with a specified value
print("\nMissing Values Replaced with 0:")
print(marks.fillna(0))


# Replace missing values with the mean
print("\nMissing Values Replaced with Mean:")
print(marks.fillna(marks.mean()))


# dropna(): Removes missing values
print("\nSeries After Removing Missing Values:")
print(marks.dropna())


# ============================================================
# 12. ARITHMETIC OPERATIONS
# ============================================================

ds = pd.Series(
    [100, 200, 300, 400],
    index=["A", "B", "C", "D"]
)

print("\nOriginal Series:")
print(ds)


# Addition
print("\nAfter Adding 100:")
print(ds + 100)


# Multiplication
print("\nAfter Multiplying by 2:")
print(ds * 2)


# Division
print("\nAfter Dividing by 50:")
print(ds / 50)


# Exponent
print("\nAfter Squaring the Values:")
print(ds ** 2)


# Modulus
print("\nRemainder After Division by 3:")
print(ds % 3)


# ============================================================
# 13. OPERATIONS BETWEEN TWO SERIES
# ============================================================

s1 = pd.Series([10, 20, 30])
s2 = pd.Series([1, 2, 3])

print("\nAddition of Two Series:")
print(s1 + s2)


# ============================================================
# 14. SERIES ALIGNMENT BY INDEX
# ============================================================

# Pandas performs operations between Series based on index labels,
# not simply by their position.

# If an index exists in only one Series, the result is NaN.

s1 = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)

s2 = pd.Series(
    [10, 20, 30],
    index=["B", "C", "D"]
)

print("\nFirst Series:")
print(s1)

print("\nSecond Series:")
print(s2)

print("\nAddition Based on Index:")
print(s1 + s2)
