# ============================================================
# Pandas - Reading CSV Files
# ============================================================

import pandas as pd


# ============================================================
# 1. Read CSV File
# ============================================================

# pd.read_csv() -> Reads a CSV file into a DataFrame.

df = pd.read_csv("csv_pandas.csv")

print(df)


# ============================================================
# 2. Read Only a Specific Number of Rows
# ============================================================

# nrows=3 -> Reads only the first 3 rows.

df = pd.read_csv(
    "csv_pandas.csv",
    nrows=3
)

print(df)


# ============================================================
# 3. View First 5 Rows
# ============================================================

df = pd.read_csv("csv_pandas.csv")

print(df.head())


# ============================================================
# 4. Check DataFrame Structure
# ============================================================

# info() -> Displays columns, data types,
# non-null values, and memory usage.

df.info()


# ============================================================
# 5. Read Specific Columns
# ============================================================

# usecols -> Reads only the selected columns.

df = pd.read_csv(
    "csv_pandas.csv",
    usecols=["DATE", "Event"]
)

print(df)


# ============================================================
# 6. Skip Rows
# ============================================================

# skiprows=2 -> Skips the first two rows.

df = pd.read_csv(
    "csv_pandas.csv",
    skiprows=2
)

print(df)


# ============================================================
# 7. Specify Header Row
# ============================================================

# header=0 -> Uses the first row as column names.

df = pd.read_csv(
    "csv_pandas.csv",
    header=0
)

print(df)


# ============================================================
# 8. Set a Column as Index
# ============================================================

# index_col -> Uses the specified column as the DataFrame index.

# Example:

df = pd.read_csv(
    "data.csv",
    index_col="Employee_ID"
)

print(df)


# ============================================================
# 9. Parse Dates While Reading the CSV
# ============================================================

# parse_dates -> Converts a date column into datetime format.

# Without parsing:
# DATE -> usually object/string

# After parsing:
# DATE -> datetime64[ns]

df = pd.read_csv(
    "csv_pandas.csv",
    parse_dates=["DATE"]
)

print(df)


# ============================================================
# 10. Extract Year from Parsed Date
# ============================================================

print(df["DATE"].dt.year)


# ============================================================
# Summary
# ============================================================

# pd.read_csv() -> Read CSV file
# nrows         -> Read a specific number of rows
# head()        -> View first rows
# info()        -> Check DataFrame structure
# usecols       -> Read selected columns
# skiprows      -> Skip rows while reading
# header        -> Specify the header row
# index_col     -> Set a column as the index
# parse_dates   -> Convert columns to datetime
