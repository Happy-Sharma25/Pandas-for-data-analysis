# ============================================================
# Pandas DataFrame - Filtering Data
# ============================================================

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

print("Employee DataFrame:")
print(df)


# ============================================================
# 2. FILTER USING A SINGLE CONDITION
# ============================================================

# Select employees with salary greater than 50,000
print("\nEmployees with Salary Greater Than 50,000:")
print(df[df["Salary"] > 50000])


# ============================================================
# 3. FILTER USING MULTIPLE CONDITIONS
# ============================================================

# AND condition:
# Both conditions must be True.

# Salary must be greater than 50,000
# AND Age must be greater than 25

print("\nSalary > 50,000 AND Age > 25:")
print(
    df[
        (df["Salary"] > 50000)
        & (df["Age"] > 25)
    ]
)


# OR condition:
# At least one condition must be True.

# Salary must be greater than 50,000
# OR Age must be greater than 25

print("\nSalary > 50,000 OR Age > 25:")
print(
    df[
        (df["Salary"] > 50000)
        | (df["Age"] > 25)
    ]
)


# ============================================================
# 4. FILTER USING isin()
# ============================================================

# isin() checks whether values belong to a specified list.

# Select employees whose salary is either 45,000 or 55,000
print("\nEmployees with Salary 45,000 or 55,000:")
print(
    df[
        df["Salary"].isin([45000, 55000])
    ]
)


# Select employees whose names are Amit or Neha
print("\nEmployees named Amit or Neha:")
print(
    df[
        df["Name"].isin(["Amit", "Neha"])
    ]
)


# ============================================================
# Summary
# ============================================================

# df[condition]              -> Filter rows
# &                          -> AND condition
# |                          -> OR condition
# isin([value1, value2])     -> Match values from a list

# ============================================================

