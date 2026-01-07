"""
Pandas Basics - Day 03: Statistical Analysis and Data Exploration
Author: Rakshith

This script demonstrates:
- Descriptive statistics
- Correlation analysis
- Value counts and frequency distributions
- Aggregation functions
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("LESSON 1: Descriptive Statistics")
print("=" * 60)

# Create a comprehensive employee dataset
np.random.seed(42)
data = {
    "employee_id": range(1, 21),
    "age": [22, 25, 30, 28, 35, 27, 32, 29, 31, 26, 
            24, 33, 28, 30, 27, 29, 31, 26, 34, 28],
    "salary": [30000, 40000, 50000, 45000, 60000, 42000, 55000, 47000, 52000, 43000,
               38000, 57000, 46000, 51000, 44000, 48000, 53000, 41000, 59000, 45000],
    "experience_years": [0, 2, 5, 3, 8, 2, 6, 4, 5, 3,
                         1, 7, 3, 5, 2, 4, 6, 2, 7, 3],
    "performance_score": [85, 90, 92, 88, 95, 87, 93, 89, 91, 86,
                          84, 94, 88, 92, 87, 89, 93, 85, 94, 88],
    "department": ["Sales", "IT", "Marketing", "IT", "Sales", "HR", "IT", "Marketing", 
                   "Sales", "HR", "IT", "Sales", "Marketing", "IT", "HR", "Sales", 
                   "IT", "Marketing", "Sales", "HR"]
}

df = pd.DataFrame(data)

print("\n Our Employee Dataset:")
print(df.head(10))

# The describe() method provides key statistics for numerical columns
print("\n Descriptive Statistics using describe():")
print(df.describe())

print("\n What these statistics mean:")
print("   count: Number of non-null values")
print("   mean:  Average value")
print("   std:   Standard deviation (measure of spread)")
print("   min:   Minimum value")
print("   25%:   First quartile (25% of data is below this)")
print("   50%:   Median (middle value)")
print("   75%:   Third quartile (75% of data is below this)")
print("   max:   Maximum value")

# Individual statistics
print("\n Individual Statistical Measures:")
print(f"   Mean salary: ${df['salary'].mean():,.2f}")
print(f"   Median salary: ${df['salary'].median():,.2f}")
print(f"   Salary standard deviation: ${df['salary'].std():,.2f}")
print(f"   Minimum age: {df['age'].min()}")
print(f"   Maximum age: {df['age'].max()}")
print(f"   Age range: {df['age'].max() - df['age'].min()}")

print("\n" + "=" * 60)
print("LESSON 2: Correlation Analysis")
print("=" * 60)

# Correlation shows the relationship between numerical variables
# Values range from -1 to 1:
#   1: Perfect positive correlation
#   0: No correlation
#  -1: Perfect negative correlation

print("\n Correlation Matrix:")
correlation_matrix = df[['age', 'salary', 'experience_years', 'performance_score']].corr()
print(correlation_matrix)

print("\n Interpreting Correlations:")
print(f"   Salary vs Experience: {correlation_matrix.loc['salary', 'experience_years']:.3f}")
print("Strong positive correlation: More experience = Higher salary")
print(f"   Salary vs Age: {correlation_matrix.loc['salary', 'age']:.3f}")
print("Moderate positive correlation: Older employees tend to earn more")
print(f"   Performance vs Salary: {correlation_matrix.loc['performance_score', 'salary']:.3f}")
print(" Moderate positive correlation: Better performance = Higher salary")

# Correlation between two specific columns
print(f"\n Correlation between salary and experience: {df['salary'].corr(df['experience_years']):.3f}")

print("\n" + "=" * 60)
print("LESSON 3: Value Counts and Distributions")
print("=" * 60)

# Value counts show frequency of each unique value
print("\n Distribution of employees by department:")
dept_counts = df['department'].value_counts()
print(dept_counts)

print("\n Department distribution as percentages:")
dept_percentages = df['department'].value_counts(normalize=True) * 100
print(dept_percentages.round(2))

# Unique values
print(f"\n Unique departments: {df['department'].unique()}")
print(f" Number of unique departments: {df['department'].nunique()}")

# Binning numerical data into categories
print("\n Age distribution (grouped into bins):")
age_bins = pd.cut(df['age'], bins=[20, 25, 30, 35, 40], labels=['20-25', '26-30', '31-35', '36-40'])
print(age_bins.value_counts().sort_index())

print("\n" + "=" * 60)
print("LESSON 4: Aggregation Functions")
print("=" * 60)

# Group by department and calculate statistics
print("\n Statistics by Department:")
dept_stats = df.groupby('department').agg({
    'salary': ['mean', 'median', 'min', 'max'],
    'age': 'mean',
    'performance_score': 'mean',
    'employee_id': 'count'  # Count of employees
})
print(dept_stats.round(2))

# Multiple aggregations on a single column
print("\n Salary statistics across all departments:")
salary_agg = df['salary'].agg(['mean', 'median', 'std', 'min', 'max'])
print(salary_agg.round(2))

# Group by and calculate custom aggregations
print("\n Department-wise analysis:")
dept_analysis = df.groupby('department').agg({
    'salary': lambda x: f"${x.mean():,.0f}",
    'experience_years': 'mean',
    'performance_score': 'mean'
}).round(2)
dept_analysis.columns = ['Avg Salary', 'Avg Experience', 'Avg Performance']
print(dept_analysis)

print("\n" + "=" * 60)
print("LESSON 5: Advanced Statistical Analysis")
print("=" * 60)

# Quantiles (percentiles)
print("\n Salary Percentiles:")
percentiles = [0.1, 0.25, 0.5, 0.75, 0.9]
salary_percentiles = df['salary'].quantile(percentiles)
for p, value in zip(percentiles, salary_percentiles):
    print(f"   {int(p*100)}th percentile: ${value:,.0f}")

# Variance and standard deviation
print(f"\n Salary variance: ${df['salary'].var():,.2f}")
print(f" Salary standard deviation: ${df['salary'].std():,.2f}")
print("   (Higher values indicate more spread in the data)")

# Coefficient of variation (relative variability)
cv_salary = (df['salary'].std() / df['salary'].mean()) * 100
print(f"\n Coefficient of variation for salary: {cv_salary:.2f}%")
print("   (Lower values indicate more consistency)")

# Skewness (measure of asymmetry)
print(f"\n Salary skewness: {df['salary'].skew():.3f}")
print("   > 0: Right-skewed (tail on right side)")
print("   < 0: Left-skewed (tail on left side)")
print("   ≈ 0: Symmetric distribution")

print("\n" + "=" * 60)
print("LESSON 6: Comparative Analysis")
print("=" * 60)

# Compare statistics across groups
print("\n Performance score by experience level:")
df['experience_level'] = pd.cut(df['experience_years'], 
                                 bins=[0, 2, 5, 10], 
                                 labels=['Junior', 'Mid', 'Senior'])
exp_performance = df.groupby('experience_level')['performance_score'].agg(['mean', 'count'])
print(exp_performance.round(2))

# Find top performers
print("\n Top 5 highest-paid employees:")
top_earners = df.nlargest(5, 'salary')[['employee_id', 'age', 'salary', 'department']]
print(top_earners)

# Find employees below/above average
avg_salary = df['salary'].mean()
print(f"\n Employees earning above average (${avg_salary:,.0f}):")
above_avg = df[df['salary'] > avg_salary].shape[0]
print(f"   Count: {above_avg} out of {len(df)} ({above_avg/len(df)*100:.1f}%)")

print("\n" + "=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("""
1. Use .describe() for quick overview of numerical data
2. Use .corr() to find relationships between variables
3. Use .value_counts() for categorical data distributions
4. Use .groupby().agg() for group-wise statistics
5. Correlation ≠ Causation: High correlation doesn't mean one causes the other
6. Use quantiles to understand data distribution beyond mean/median
7. Always visualize data alongside statistics for better insights
""")

