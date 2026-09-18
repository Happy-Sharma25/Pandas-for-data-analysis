# ============================================================
# Pandas DataFrame - Rename and Drop Data
# ============================================================

import pandas as pd


# ============================================================
# 1. CREATE A DATAFRAME
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Salary": [35000, 50000, 45000, 38000]
})

print("Original DataFrame:")
print(df)


# ============================================================
# 2. RENAME A COLUMN
# ============================================================

# rename() is used to change column names.

df = df.rename(
    columns={"Salary": "Monthly Salary"}
)

print("\nColumn Names After Renaming:")
print(df.columns)

print("\nDataFrame After Renaming:")
print(df)


# ============================================================
# 3. DROP A COLUMN
# ============================================================

# drop() removes the specified column.

# axis is not required when using columns=.

df = df.drop(columns="Monthly Salary")

print("\nDataFrame After Dropping Salary Column:")
print(df)


# ============================================================
# 4. DROP A ROW
# ============================================================

# Delete the row with index 1.
df = df.drop(index=1)

print("\nDataFrame After Dropping Row with Index 1:")
print(df)


# ============================================================
# Summary
# ============================================================

# df.rename(columns={...})
#     -> Rename one or more columns

# df.drop(columns="Column")
#     -> Remove a column

# df.drop(index=1)
#     -> Remove a row using its index

# ============================================================
