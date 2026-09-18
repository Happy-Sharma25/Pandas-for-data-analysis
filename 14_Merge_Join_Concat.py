# ============================================================
# Pandas - Merge, Join and Concat
# ============================================================

import pandas as pd


# ============================================================
# 1. Create Employees DataFrame
# ============================================================

employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104],
    "Name": ["Amit", "Priya", "Rahul", "Neha"]
})

print(employees)


# ============================================================
# 2. Create Salary DataFrame
# ============================================================

salary = pd.DataFrame({
    "Emp_ID": [101, 102, 104, 105],
    "Salary": [35000, 50000, 38000, 45000]
})

print(salary)


# ============================================================
# 3. Inner Merge
# ============================================================

# Inner merge keeps only matching Emp_ID values from both DataFrames.

result = pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="inner"
)

print(result)

# Matching IDs: 101, 102, 104


# ============================================================
# 4. Left Merge
# ============================================================

# Left merge keeps all rows from the left DataFrame.
# Missing matches from the right DataFrame become NaN.

result = pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="left"
)

print(result)


# ============================================================
# 5. Right Merge
# ============================================================

# Right merge keeps all rows from the right DataFrame.
# Missing matches from the left DataFrame become NaN.

result = pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="right"
)

print(result)


# ============================================================
# 6. Outer Merge
# ============================================================

# Outer merge keeps all rows from both DataFrames.
# Missing values are represented as NaN.

result = pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="outer"
)

print(result)


# ============================================================
# 7. Join
# ============================================================

# join() is similar to merge().
# By default, join() matches DataFrames using their indexes.

df1 = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"]
}, index=[101, 102, 103])

df2 = pd.DataFrame({
    "Salary": [35000, 50000, 45000]
}, index=[101, 102, 103])

result = df1.join(df2)

print(result)

# No "on=" is required because both DataFrames
# are joined using their indexes.


# ============================================================
# 8. Concat - Row-wise
# ============================================================

# concat() combines DataFrames along an axis.
# axis=0 is the default and adds rows vertically.

result = pd.concat([df1, df2])

print(result)


# ============================================================
# 9. Concat - Column-wise
# ============================================================

# axis=1 combines DataFrames horizontally.
# Matching is performed using the index.

result = pd.concat([df1, df2], axis=1)

print(result)


# ============================================================
# Summary
# ============================================================

# merge() -> Combine DataFrames using one or more columns

# inner -> Keep matching rows from both DataFrames
# left  -> Keep all rows from the left DataFrame
# right -> Keep all rows from the right DataFrame
# outer -> Keep all rows from both DataFrames

# join() -> Combine DataFrames using the index by default

# concat() -> Combine DataFrames vertically or horizontally
# axis=0  -> Row-wise
# axis=1  -> Column-wise
