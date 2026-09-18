# ============================================================
# Pandas DataFrame - Selecting and Filtering Data
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
# 2. SELECT COLUMNS
# ============================================================

# Select a single column
# Output type: Series
print("\nName Column:")
print(df["Name"])


# Select multiple columns
# Output type: DataFrame
print("\nName and Salary Columns:")
print(df[["Name", "Salary"]])


# ============================================================
# 3. SELECT ROWS USING iloc
# ============================================================

# iloc = integer location
# It selects rows and columns using their integer positions.

# Select the first row
print("\nFirst Row:")
print(df.iloc[0])


# Select the third row
print("\nThird Row:")
print(df.iloc[2])


# Select multiple rows
print("\nFirst, Third and Fifth Rows:")
print(df.iloc[[0, 2, 4]])


# ============================================================
# 4. ROW SLICING USING iloc
# ============================================================

# Select rows from index 1 up to, but not including, index 4
print("\nRows 1 to 3:")
print(df.iloc[1:4])


# ============================================================
# 5. SELECT ROW AND COLUMN USING iloc
# ============================================================

# Row 0, Column 1
# Column 1 is the Age column
print("\nAge of First Employee:")
print(df.iloc[0, 1])


# Select first 3 rows and first 2 columns
print("\nFirst 3 Rows and First 2 Columns:")
print(df.iloc[0:3, 0:2])


# Select specific rows and columns
# Rows: 0, 2
# Columns: 1, 3
print("\nSelected Rows and Columns:")
print(df.iloc[[0, 2], [1, 3]])


# ============================================================
# 6. SELECT ROWS USING loc
# ============================================================

# loc selects data using row/column labels.

# Select the row with label 0
print("\nRow with Label 0:")
print(df.loc[0])


# Select multiple rows using labels
print("\nRows with Labels 0 and 3:")
print(df.loc[[0, 3]])


# Select a specific row and column
print("\nSalary of First Employee:")
print(df.loc[0, "Salary"])


# Select multiple rows and columns
print("\nName and Salary of Selected Employees:")
print(df.loc[[0, 3], ["Name", "Salary"]])


# ============================================================
# 7. FILTER ROWS USING CONDITIONS
# ============================================================

# Select employees with salary greater than 40,000
print("\nEmployees with Salary Greater Than 40,000:")
print(df[df["Salary"] > 40000])


# Select employees from the HR department
print("\nEmployees from HR Department:")
print(df[df["Department"] == "HR"])


# ============================================================
# 8. FILTER USING MULTIPLE CONDITIONS
# ============================================================

# AND condition:
# Department must be IT AND Salary must be greater than 40,000
print("\nIT Employees with Salary Greater Than 40,000:")
print(
    df[
        (df["Department"] == "IT")
        & (df["Salary"] > 40000)
    ]
)


# OR condition:
# Select employees who are from HR OR IT
print("\nEmployees from HR or IT:")
print(
    df[
        (df["Department"] == "HR")
        | (df["Department"] == "IT")
    ]
)


# ============================================================
# Summary
# ============================================================

# df["Column"]              -> Select one column
# df[["Col1", "Col2"]]      -> Select multiple columns
# df.iloc[]                 -> Select using integer positions
# df.loc[]                  -> Select using labels
# df[condition]             -> Filter rows using conditions
# &                         -> AND condition
# |                         -> OR condition

# ============================================================
