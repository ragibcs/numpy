import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv('/mnt/win_iv/numpy/Bd_Employee_dataset/Bd_Employee_Data.csv')

# Checking the missing values
print("Missing values in each Column:")
print(df.isnull().sum())

# Fill missing values
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Rating'].fillna(df['Performance_Rating'].median(), inplace=True)

# Replace inf values
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Replace negative salaries
df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(), df['Salary'])

# Remove outliers using 3-sigma rule
salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# Remove rows where salary is too high or too low
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

# Save cleaned data
df.to_csv('cleaned_bd_employee_data.csv', index=False)
print('Data Cleaning Completed. Saved as cleaned_bd_employee_data.csv')