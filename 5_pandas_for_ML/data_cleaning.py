"""
Pandas Basics - Day 02: Data Cleaning and Handling Missing Values
Author: Rakshith

This script demonstrates:
- Detecting missing values
- Different strategies for handling missing data
- When to use mean vs median vs mode
- Dropping vs filling missing values
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("LESSON 1: Detecting Missing Values")
print("=" * 60)

# Create a DataFrame with missing values
data = {
    "employee_id": [101, 102, 103, 104, 105, 106],
    "name": ["Alice", "Bob", None, "Diana", "Eve", "Frank"],
    "age": [22, 25, None, 30, 28, 35],
    "salary": [30000, None, 50000, 45000, 48000, None],
    "department": ["Sales", "IT", "Marketing", None, "Sales", "IT"],
    "performance_score": [85, 90, 78, None, 92, 88]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# Check for missing values (returns True/False for each cell)
print("\n Missing value detection using isnull():")
print(df.isnull())

# Count missing values per column
print("\n Count of missing values per column:")
print(df.isnull().sum())

# Check if ANY value is missing in each row
print("\n Rows with any missing values:")
print(df[df.isnull().any(axis=1)])

# Get percentage of missing values per column
print("\n Percentage of missing values:")
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent)

print("\n" + "=" * 60)
print("LESSON 2: Filling Missing Values - Strategies")
print("=" * 60)

# Create a copy to preserve original data
df_filled = df.copy()

# Strategy 1: Fill with MEAN (best for normally distributed numerical data)
# Use mean when data doesn't have extreme outliers
print("\n Strategy 1: Fill 'age' with MEAN")
age_mean = df_filled["age"].mean()
print(f"   Mean age: {age_mean:.2f}")
df_filled["age"] = df_filled["age"].fillna(age_mean)

# Strategy 2: Fill with MEDIAN (best for skewed data or data with outliers)
# Median is more robust to extreme values than mean
print("\n Strategy 2: Fill 'salary' with MEDIAN")
salary_median = df_filled["salary"].median()
print(f"   Median salary: ${salary_median:,.0f}")
df_filled["salary"] = df_filled["salary"].fillna(salary_median)

# Strategy 3: Fill with MODE (best for categorical data)
# Mode is the most frequent value
print("\n Strategy 3: Fill 'department' with MODE")
department_mode = df_filled["department"].mode()[0]
print(f"   Most common department: {department_mode}")
df_filled["department"] = df_filled["department"].fillna(department_mode)

# Strategy 4: Fill with a specific value
print("\n Strategy 4: Fill 'performance_score' with specific value (0)")
df_filled["performance_score"] = df_filled["performance_score"].fillna(0)

# Strategy 5: Forward fill (use previous value)
print("\n Strategy 5: Fill 'name' with forward fill")
df_filled["name"] = df_filled["name"].fillna(method='ffill')

print("\ DataFrame after filling missing values:")
print(df_filled)

print("\n" + "=" * 60)
print("LESSON 3: Dropping Missing Values")
print("=" * 60)

# Create another copy
df_dropped = df.copy()

# Drop rows with ANY missing value
print("\n Option 1: Drop rows with ANY missing value")
df_dropped_any = df_dropped.dropna()
print(f"   Original rows: {len(df)}")
print(f"   After dropping: {len(df_dropped_any)}")
print(df_dropped_any)

# Drop rows where ALL values are missing
print("\n Option 2: Drop rows where ALL values are missing")
df_dropped_all = df_dropped.dropna(how='all')
print(f"   Rows remaining: {len(df_dropped_all)}")

# Drop rows with missing values in specific columns
print("\n Option 3: Drop rows with missing values in 'salary' column")
df_dropped_subset = df_dropped.dropna(subset=['salary'])
print(df_dropped_subset)

# Drop columns with missing values
print("\n Option 4: Drop columns with any missing value")
df_dropped_cols = df_dropped.dropna(axis=1)
print(df_dropped_cols)

print("\n" + "=" * 60)
print("LESSON 4: Advanced Filling Techniques")
print("=" * 60)

# Interpolation for time series or sequential data
data_sequential = {
    "day": [1, 2, 3, 4, 5, 6],
    "temperature": [20, 22, None, 26, None, 30]
}
df_temp = pd.DataFrame(data_sequential)

print("\n Temperature data with missing values:")
print(df_temp)

# Linear interpolation estimates missing values based on surrounding values
df_temp["temperature_interpolated"] = df_temp["temperature"].interpolate()
print("\n After linear interpolation:")
print(df_temp)

# Fill with group-specific values (e.g., department average)
print("\n Fill salary based on department average:")
df_grouped = df.copy()
df_grouped["salary"] = df_grouped.groupby("department")["salary"].transform(
    lambda x: x.fillna(x.mean())
)
print(df_grouped[["name", "department", "salary"]])

print("\n" + "=" * 60)
print("LESSON 5: Best Practices Decision Tree")
print("=" * 60)

print("""
 When to use each strategy:

NUMERICAL DATA:
  ├─ Normally distributed, no outliers → Use MEAN
  ├─ Skewed or has outliers → Use MEDIAN
  ├─ Sequential/time series → Use INTERPOLATION
  └─ Group-specific patterns → Use GROUP MEAN/MEDIAN

CATEGORICAL DATA:
  ├─ Use MODE (most frequent value)
  └─ If logical order exists → Use FORWARD FILL or BACKWARD FILL

TEXT DATA:
  ├─ Use "Unknown" or "Not Specified"
  └─ Or use MODE if categories exist

WHEN TO DROP:
  ├─ Missing > 50% of data in a column → Drop the column
  ├─ Missing data is critical (e.g., ID, key field) → Drop the row
  └─ Small dataset with few missing values → Drop rows

GENERAL RULE:
  → Always understand WHY data is missing before deciding how to handle it
  → Document your decision-making process
  → Keep a copy of original data before cleaning
""")

print("\n" + "=" * 60)
print(" Key Takeaways:")
print("=" * 60)
print("""
1. Use .isnull() and .isnull().sum() to detect missing values
2. Use .fillna() to fill missing values with mean, median, mode, or custom values
3. Use .dropna() to remove rows or columns with missing data
4. Use .interpolate() for sequential/time series data
5. Use .groupby().transform() for group-specific filling
6. Always consider the context before choosing a strategy
""")

print("\n Next: Learn about statistical analysis in 03_data_analysis.py")