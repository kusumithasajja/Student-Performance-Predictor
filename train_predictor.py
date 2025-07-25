import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('student_data.csv')

# Features and target
X = df[['Attendance', 'Previous_Marks', 'Hours_Studied', 'Participation']]
y = df['Final_Score']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')

# Show coefficients
print('\nModel Coefficients:')
for feature, coef in zip(X.columns, model.coef_):
    print(f'{feature}: {coef:.2f}')

# Predict for a new student (example)
def predict_new(attendance, previous_marks, hours_studied, participation):
    data = pd.DataFrame({
        'Attendance': [attendance],
        'Previous_Marks': [previous_marks],
        'Hours_Studied': [hours_studied],
        'Participation': [participation]
    })
    pred = model.predict(data)[0]
    print(f'Predicted Final Score: {pred:.2f}')

# Example usage
print('\nExample Prediction:')
predict_new(attendance=90, previous_marks=85, hours_studied=10, participation=4) 