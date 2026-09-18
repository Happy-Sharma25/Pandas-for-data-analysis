# ============================================================
# Pandas DataFrame - Handling Duplicate Rows
# ============================================================

import pandas as pd


# ============================================================
# 1. Create DataFrame
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Priya", "Neha", "Rahul"],
    "Age": [25, 30, 28, 30, 26, 28],
    "Salary": [35000, 50000, 45000, 50000, 38000, 45000]
})

print(df)


# ============================================================
# 2. Check Duplicate Rows
# ============================================================

# duplicated() checks whether each row is a duplicate.
# First occurrence = False
# Duplicate occurrence = True

print(df.duplicated())


# ============================================================
# 3. View Only Duplicate Rows
# ============================================================

print(df[df.duplicated()])


# ============================================================
# 4. Count Duplicate Rows
# ============================================================

print(df.duplicated().sum())


# ============================================================
# 5. Remove Duplicate Rows
# ============================================================

print(df.drop_duplicates())


# ============================================================
# 6. Remove Duplicates and Reset Index
# ============================================================

print(df.drop_duplicates(ignore_index=True))


# ============================================================
# Summary
# ============================================================

# duplicated()       -> Identifies duplicate rows
# drop_duplicates()  -> Removes duplicate rows
# sum()              -> Counts duplicate rows
# ignore_index=True  -> Resets the index after removing duplicates
