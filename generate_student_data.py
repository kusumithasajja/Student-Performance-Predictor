import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

num_students = 200

data = {
    'StudentID': np.arange(1, num_students + 1),
    'Attendance': np.random.randint(60, 101, num_students),  # 60% to 100%
    'Previous_Marks': np.random.randint(40, 101, num_students),  # 40 to 100
    'Hours_Studied': np.random.randint(0, 21, num_students),  # 0 to 20 hours/week
    'Participation': np.random.randint(1, 6, num_students),  # 1 (low) to 5 (high)
}

# Simulate Final Score with some noise
# Weights: Attendance (0.2), Previous_Marks (0.4), Hours_Studied (0.3), Participation (0.1)
noise = np.random.normal(0, 5, num_students)
data['Final_Score'] = (
    0.2 * data['Attendance'] +
    0.4 * data['Previous_Marks'] +
    0.3 * data['Hours_Studied'] * 5 +  # scale hours
    0.1 * data['Participation'] * 20 +
    noise
)
data['Final_Score'] = np.clip(data['Final_Score'], 0, 100)

df = pd.DataFrame(data)
df.to_csv('student_data.csv', index=False)

print('Synthetic student dataset generated and saved as student_data.csv') 