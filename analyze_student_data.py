import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('student_data.csv')

# Show first few rows
print('First 5 rows:')
print(df.head())

# Show basic statistics
print('\nStatistics:')
print(df.describe())

# Check for missing values
print('\nMissing values:')
print(df.isnull().sum())

# Visualize relationships
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(df['Attendance'], df['Final_Score'], alpha=0.7)
plt.xlabel('Attendance (%)')
plt.ylabel('Final Score')
plt.title('Attendance vs Final Score')

plt.subplot(1, 2, 2)
plt.scatter(df['Hours_Studied'], df['Final_Score'], alpha=0.7, color='orange')
plt.xlabel('Hours Studied')
plt.ylabel('Final Score')
plt.title('Hours Studied vs Final Score')

plt.tight_layout()
plt.show() 