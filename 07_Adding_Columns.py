# ============================================================
# Pandas DataFrame - Adding and Inserting Columns
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
# 2. ADD A COLUMN WITH A FIXED VALUE
# ============================================================

# The same bonus amount is assigned to every row.
df["Bonus"] = 5000

print("\nAfter Adding Bonus:")
print(df)


# ============================================================
# 3. ADD A COLUMN USING A CALCULATION
# ============================================================

# Calculate total salary including bonus.
df["Total"] = df["Salary"] + df["Bonus"]

print("\nAfter Calculating Total Salary:")
print(df)


# ============================================================
# 4. ADD A COLUMN USING A PERCENTAGE INCREMENT
# ============================================================

# Increase the salary by 10%.
df["New_Salary"] = df["Salary"] * 1.10

print("\nAfter 10% Salary Increment:")
print(df)


# ============================================================
# 5. ADD A COLUMN USING A LIST
# ============================================================

# The number of values in the list must match
# the number of rows in the DataFrame.

df["Department"] = ["HR", "Sales", "IT", "HR"]

print("\nAfter Adding Department:")
print(df)


# ============================================================
# 6. INSERT A COLUMN AT A SPECIFIC POSITION
# ============================================================

# insert() syntax:
# df.insert(position, column_name, value)

# Position 1 means the second column.

df.insert(1, "Tax", 800)

print("\nAfter Inserting Tax Column:")
print(df)


# ============================================================
# Summary
# ============================================================

# df["Column"] = value
#     -> Add a column with the same value for every row

# df["New_Column"] = calculation
#     -> Create a column using existing columns

# df["Column"] = list
#     -> Add a column using a list of values

# df.insert()
#     -> Insert a column at a specific position

# ============================================================
