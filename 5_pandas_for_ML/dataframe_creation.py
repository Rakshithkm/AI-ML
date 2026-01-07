"""
Pandas Basics - Day 01: DataFrame Creation and Inspection
Author: Rakshith

This script demonstrates:
- Creating DataFrames from dictionaries
- Inspecting DataFrame structure
- Understanding data types
- Basic DataFrame information
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("LESSON 1: Creating DataFrames from Dictionaries")
print("=" * 60)

# Create a DataFrame from a dictionary
# Each key becomes a column name, and values become the column data
employee_data = {
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["Alice Johnson", "Bob Smith", "Charlie Davis", "Diana Miller", "Eve Wilson"],
    "age": [22, 25, 30, None, 28],
    "department": ["Sales", "IT", "Marketing", "IT", "Sales"],
    "salary": [30000, 40000, 50000, 45000, None],
    "experience_years": [0, 2, 5, 3, 4]
}

df = pd.DataFrame(employee_data)

print("\n Our Employee DataFrame:")
print(df)

print("\n" + "=" * 60)
print("LESSON 2: Inspecting DataFrame Structure")
print("=" * 60)

# Show first few rows (default is 5)
print("\n First 3 rows using head():")
print(df.head(3))

# Show last few rows
print("\n Last 2 rows using tail():")
print(df.tail(2))

# Get DataFrame shape (rows, columns)
print(f"\n DataFrame shape: {df.shape}")
print(f"   → {df.shape[0]} rows and {df.shape[1]} columns")

# Get column names
print(f"\n Column names: {df.columns.tolist()}")

# Get index (row labels)
print(f"\n Index: {df.index.tolist()}")

print("\n" + "=" * 60)
print("LESSON 3: Understanding Data Types")
print("=" * 60)

# Check data types of each column
print("\n Data types of each column:")
print(df.dtypes)
print("\nNote: 'object' type usually means text/string data")
print("      'float64' means decimal numbers")
print("      'int64' means whole numbers")

# Get detailed information about the DataFrame
print("\n Detailed DataFrame information:")
print(df.info())

print("\n" + "=" * 60)
print("LESSON 4: Accessing Specific Data")
print("=" * 60)

# Access a single column (returns a Series)
print("\n Accessing 'name' column:")
print(df["name"])

# Access multiple columns (returns a DataFrame)
print("\n Accessing multiple columns ['name', 'salary']:")
print(df[["name", "salary"]])

# Access a single row by index position using iloc
print("\n Accessing row at index 2 using iloc:")
print(df.iloc[2])

# Access a specific cell value
print(f"\n Salary of employee at index 1: ${df.loc[1, 'salary']:,.0f}")

print("\n" + "=" * 60)
print("LESSON 5: Creating DataFrames from Other Sources")
print("=" * 60)

# Create DataFrame from a list of lists
print("\n Creating DataFrame from list of lists:")
data_lists = [
    ["Product A", 100, 25.50],
    ["Product B", 150, 30.00],
    ["Product C", 200, 22.75]
]
df_products = pd.DataFrame(data_lists, columns=["Product", "Quantity", "Price"])
print(df_products)

# Create DataFrame from a NumPy array
print("\n Creating DataFrame from NumPy array:")
np_array = np.random.randint(1, 100, size=(3, 3))
df_numpy = pd.DataFrame(np_array, columns=["Col1", "Col2", "Col3"])
print(df_numpy)

print("\n" + "=" * 60)
print(" Key Takeaways:")
print("=" * 60)
print("""
1. DataFrames are created using pd.DataFrame() with dict, lists, or arrays
2. Use .head() and .tail() to preview data
3. Use .shape to get dimensions, .columns for column names
4. Use .dtypes to check data types, .info() for detailed overview
5. Access columns with df['column'] or df[['col1', 'col2']]
6. Access rows with .iloc[index] or .loc[label]
""")

print("\n Next: Learn about handling missing values in 02_data_cleaning.py")