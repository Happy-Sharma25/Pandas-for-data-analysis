# ============================================================
# Pandas DataFrame - Date and Time Operations
# ============================================================

import pandas as pd


# ============================================================
# 1. Create DataFrame
# ============================================================

df = pd.DataFrame({
    "Order Date": [
        "2026-07-01",
        "2026-08-15",
        "2026-09-20"
    ]
})

print(df)


# ============================================================
# 2. Check Data Type
# ============================================================

# Dates are initially stored as strings.

print(df.dtypes)


# ============================================================
# 3. Convert String to Datetime
# ============================================================

# pd.to_datetime() -> Converts strings into Pandas datetime objects.

df["Order Date"] = pd.to_datetime(df["Order Date"])

print(df)
print(df.dtypes)


# ============================================================
# 4. Extract Year
# ============================================================

# .dt.year -> Extracts the year from a date.

print(df["Order Date"].dt.year)

# Add year as a new column.
df["Year"] = df["Order Date"].dt.year

print(df)


# ============================================================
# 5. Extract Month
# ============================================================

# .dt.month -> Extracts the month number.

print(df["Order Date"].dt.month)


# ============================================================
# 6. Extract Day
# ============================================================

# .dt.day -> Extracts the day of the month.

print(df["Order Date"].dt.day)


# ============================================================
# 7. Extract Day Name
# ============================================================

# .dt.day_name() -> Returns the name of the day.

print(df["Order Date"].dt.day_name())


# ============================================================
# 8. Extract Weekday Number
# ============================================================

# .dt.weekday -> Returns the weekday as a number.
# 0 = Monday
# 6 = Sunday

print(df["Order Date"].dt.weekday)


# ============================================================
# 9. Other Useful Date and Time Attributes
# ============================================================

# .dt.date         -> Returns only the date
# .dt.time         -> Returns only the time
# .dt.minute       -> Extracts the minute
# .dt.second       -> Extracts the second
# .dt.day_name()   -> Returns the day name
# .dt.month_name() -> Returns the month name
# .dt.quarter      -> Returns the quarter (1-4)
# .dt.dayofyear    -> Returns the day number of the year


# ============================================================
# Summary
# ============================================================

# pd.to_datetime() -> Convert values to datetime
# .dt.year        -> Extract year
# .dt.month       -> Extract month number
# .dt.day         -> Extract day of month
# .dt.day_name()  -> Extract day name
# .dt.weekday     -> Extract weekday number
# .dt.quarter     -> Extract quarter
