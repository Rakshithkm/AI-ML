"""
Pandas Basics - Day 04: Data Transformation and Manipulation
Author: Rakshith

This script demonstrates:
- Filtering and querying data
- Sorting operations
- Creating new columns
- Applying functions
- Merging and joining DataFrames
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("LESSON 1: Filtering Data")
print("=" * 60)

# Create sample dataset
np.random.seed(42)
employees = pd.DataFrame({
    "employee_id": range(1, 16),
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", 
             "Henry", "Iris", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia"],
    "age": [22, 25, 30, 28, 35, 27, 32, 29, 31, 26, 24, 33, 28, 30, 27],
    "salary": [30000, 40000, 50000, 45000, 60000, 42000, 55000, 47000, 
               52000, 43000, 38000, 57000, 46000, 51000, 44000],
    "department": ["Sales", "IT", "Marketing", "IT", "Sales", "HR", "IT", 
                   "Marketing", "Sales", "HR", "IT", "Sales", "Marketing", "IT", "HR"],
    "performance_score": [85, 90, 92, 88, 95, 87, 93, 89, 91, 86, 84, 94, 88, 92, 87]
})

print("\n Original Employee Dataset:")
print(employees.head(10))

# Basic filtering with boolean indexing
print("\n Filter 1: Employees with salary > $45,000")
high_earners = employees[employees['salary'] > 45000]
print(high_earners[['name', 'salary', 'department']])

# Multiple conditions with & (AND) and | (OR)
print("\n Filter 2: IT employees with performance score > 90")
top_it = employees[(employees['department'] == 'IT') & (employees['performance_score'] > 90)]
print(top_it[['name', 'department', 'performance_score']])

print("\n Filter 3: Sales OR HR employees")
sales_hr = employees[(employees['department'] == 'Sales') | (employees['department'] == 'HR')]
print(f"Count: {len(sales_hr)}")
print(sales_hr[['name', 'department']])

# Using .isin() for multiple values
print("\n Filter 4: Employees in specific departments using isin()")
selected_depts = employees[employees['department'].isin(['IT', 'Marketing'])]
print(f"Count: {len(selected_depts)}")

# Using .query() method (more readable for complex queries)
print("\n Filter 5: Using query() method")
query_result = employees.query('age >= 30 and salary > 50000')
print(query_result[['name', 'age', 'salary']])

# String filtering
print("\n Filter 6: Names starting with 'M'")
names_with_m = employees[employees['name'].str.startswith('M')]
print(names_with_m[['name', 'department']])

print("\n" + "=" * 60)
print("LESSON 2: Sorting Data")
print("=" * 60)

# Sort by a single column
print("\n Sort by salary (ascending):")
sorted_salary = employees.sort_values('salary').head(5)
print(sorted_salary[['name', 'salary']])

# Sort in descending order
print("\n Sort by salary (descending):")
sorted_salary_desc = employees.sort_values('salary', ascending=False).head(5)
print(sorted_salary_desc[['name', 'salary']])

# Sort by multiple columns
print("\n Sort by department, then by salary (within each department):")
multi_sort = employees.sort_values(['department', 'salary'], ascending=[True, False])
print(multi_sort[['name', 'department', 'salary']])

# Sort by index
print("\n Sort by index (employee_id in reverse):")
sorted_index = employees.sort_index(ascending=False).head(5)
print(sorted_index[['employee_id', 'name']])

print("\n" + "=" * 60)
print("LESSON 3: Creating New Columns")
print("=" * 60)

# Create a copy to avoid modifying original
df = employees.copy()

# Simple calculation
print("\n Create 'annual_bonus' column (10% of salary):")
df['annual_bonus'] = df['salary'] * 0.10
print(df[['name', 'salary', 'annual_bonus']].head())

# Conditional column using np.where()
print("\n Create 'salary_category' based on salary amount:")
df['salary_category'] = np.where(df['salary'] >= 50000, 'High', 'Medium')
df['salary_category'] = np.where(df['salary'] < 40000, 'Low', df['salary_category'])
print(df[['name', 'salary', 'salary_category']].head(8))

# Using .apply() with a custom function
print("\n Create 'performance_level' using apply():")
def categorize_performance(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 85:
        return 'Good'
    else:
        return 'Average'

df['performance_level'] = df['performance_score'].apply(categorize_performance)
print(df[['name', 'performance_score', 'performance_level']].head(8))

# Using lambda function
print("\n Create 'age_group' using lambda:")
df['age_group'] = df['age'].apply(lambda x: '20-25' if x <= 25 else ('26-30' if x <= 30 else '31+'))
print(df[['name', 'age', 'age_group']].head(8))

# Combining multiple columns
print("\n Create 'total_compensation' (salary + bonus):")
df['total_compensation'] = df['salary'] + df['annual_bonus']
print(df[['name', 'salary', 'annual_bonus', 'total_compensation']].head())

print("\n" + "=" * 60)
print("LESSON 4: Applying Functions to Data")
print("=" * 60)

# Apply function to entire DataFrame
print("\n Round all numerical values to 2 decimal places:")
numerical_cols = df.select_dtypes(include=[np.number]).columns
df[numerical_cols] = df[numerical_cols].round(2)

# Apply function to specific column
print("\n Convert names to uppercase:")
df['name_upper'] = df['name'].str.upper()
print(df[['name', 'name_upper']].head())

# Apply function row-wise (axis=1)
print("\n Create 'summary' column combining multiple fields:")
def create_summary(row):
    return f"{row['name']} ({row['department']}) - ${row['salary']:,}"

df['summary'] = df.apply(create_summary, axis=1)
print(df['summary'].head())

# Transform data within groups
print("\n Calculate salary as percentage of department average:")
df['pct_of_dept_avg'] = df.groupby('department')['salary'].transform(
    lambda x: (x / x.mean()) * 100
).round(2)
print(df[['name', 'department', 'salary', 'pct_of_dept_avg']].head(8))

print("\n" + "=" * 60)
print("LESSON 5: Merging and Joining DataFrames")
print("=" * 60)

# Create additional DataFrames for merging
projects = pd.DataFrame({
    "employee_id": [1, 2, 3, 4, 5, 6, 7, 8, 16, 17],
    "project_name": ["Project A", "Project B", "Project A", "Project C", "Project B",
                     "Project D", "Project C", "Project A", "Project E", "Project F"],
    "hours_worked": [120, 100, 150, 80, 110, 90, 130, 140, 95, 105]
})

locations = pd.DataFrame({
    "employee_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "city": ["New York", "Boston", "Chicago", "Boston", "New York", 
             "Chicago", "Boston", "New York", "Chicago", "Boston"]
})

print("\n Employees DataFrame (first 5 rows):")
print(employees[['employee_id', 'name', 'department']].head())

print("\n Projects DataFrame:")
print(projects.head())

print("\n Locations DataFrame:")
print(locations.head())

# Inner join (only matching records)
print("\n Inner Join: Employees with assigned projects")
inner_merged = pd.merge(employees[['employee_id', 'name', 'department']], 
                        projects, 
                        on='employee_id', 
                        how='inner')
print(inner_merged.head(8))

# Left join (all employees, with projects where available)
print("\n Left Join: All employees with their projects (if any)")
left_merged = pd.merge(employees[['employee_id', 'name', 'department']], 
                       projects, 
                       on='employee_id', 
                       how='left')
print(f"Total rows: {len(left_merged)} (includes employees without projects)")
print(left_merged.head(8))

# Multiple joins
print("\n Multiple Joins: Employees with projects and locations")
full_data = pd.merge(employees[['employee_id', 'name', 'department']], 
                     projects, 
                     on='employee_id', 
                     how='left')
full_data = pd.merge(full_data, 
                     locations, 
                     on='employee_id', 
                     how='left')
print(full_data.head(8))

# Concatenating DataFrames (stacking)
print("\n Concatenating DataFrames vertically:")
df1 = employees.head(3)
df2 = employees.tail(3)
concatenated = pd.concat([df1, df2], ignore_index=True)
print(concatenated[['employee_id', 'name', 'department']])

print("\n" + "=" * 60)
print(" Key Takeaways:")
print("=" * 60)
print("""
1. Filter data using boolean indexing: df[df['column'] > value]
2. Use & for AND, | for OR in multiple conditions
3. Use .query() for more readable complex filters
4. Sort with .sort_values(), specify ascending=False for descending
5. Create columns with simple assignment: df['new'] = calculation
6. Use .apply() for complex transformations with custom functions
7. Use pd.merge() to join DataFrames on common columns
8. Use pd.concat() to stack DataFrames vertically
9. Use .transform() with .groupby() for group-wise calculations
""")

