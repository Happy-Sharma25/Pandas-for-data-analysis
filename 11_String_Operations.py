# ============================================================
# Pandas Series - String Operations
# ============================================================

import pandas as pd


# ============================================================
# 1. Create DataFrame
# ============================================================

df = pd.DataFrame({
    "Name": ["amit", " PRIYA ", "rahul kumar", "NeHa"],
    "Email": [
        "amit@gmail.com",
        "priya@yahoo.com",
        "rahul@gmail.com",
        "neha@hotmail.com"
    ]
})

print(df)


# ============================================================
# 2. Convert Text to Uppercase
# ============================================================

# str.upper() -> Converts all text to uppercase.

print(df["Name"].str.upper())


# ============================================================
# 3. Convert Text to Lowercase
# ============================================================

# str.lower() -> Converts all text to lowercase.

print(df["Email"].str.lower())


# ============================================================
# 4. Convert Text to Title Case
# ============================================================

# str.title() -> Capitalizes the first letter of each word.

print(df["Name"].str.title())


# ============================================================
# 5. Remove Extra Spaces
# ============================================================

# str.strip() -> Removes spaces from the beginning and end.

print(df["Name"].str.strip())


# ============================================================
# 6. Replace Part of a String
# ============================================================

# str.replace() -> Replaces matching text with new text.

print(df["Email"].str.replace("gmail.com", "company.com"))


# ============================================================
# 7. Check Whether Text Contains a Pattern
# ============================================================

# str.contains() -> Checks whether a string contains a pattern.

print(df["Email"].str.contains("gmail"))

# View rows where the email contains "gmail".
print(df[df["Email"].str.contains("gmail")])


# ============================================================
# 8. Check Whether Text Starts With a Pattern
# ============================================================

# str.startswith() -> Checks whether text starts with a pattern.

print(df["Email"].str.startswith("amit"))

# View emails that start with "amit".
print(df[df["Email"].str.startswith("amit")])


# ============================================================
# 9. Check Whether Text Ends With a Pattern
# ============================================================

# str.endswith() -> Checks whether text ends with a pattern.

print(df["Email"].str.endswith(".com"))


# ============================================================
# 10. Split Text
# ============================================================

# str.split() -> Splits text into a list using a separator.

print(df["Email"].str.split("@"))


# ============================================================
# 11. Count Characters
# ============================================================

# str.len() -> Returns the number of characters in each string.
# Spaces are also counted as characters.

print(df["Email"].str.len())


# ============================================================
# Summary
# ============================================================

# str.upper()       -> Convert text to uppercase
# str.lower()       -> Convert text to lowercase
# str.title()       -> Convert text to title case
# str.strip()       -> Remove leading and trailing spaces
# str.replace()     -> Replace text
# str.contains()    -> Check whether text contains a pattern
# str.startswith()  -> Check how text begins
# str.endswith()    -> Check how text ends
# str.split()       -> Split text into a list
# str.len()         -> Count characters
