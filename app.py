from flask import Flask, render_template_string, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load data and train model on startup
df = pd.read_csv('student_data.csv')
X = df[['Attendance', 'Previous_Marks', 'Hours_Studied', 'Participation']]
y = df['Final_Score']
model = LinearRegression()
model.fit(X, y)

# HTML template
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Student Performance Predictor</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            background: url('{{ url_for('static', filename='image.png') }}') center center/cover no-repeat fixed;
            filter: brightness(1.15);
        }
        .container {
            max-width: 400px;
            background: #111;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.20);
            color: #fff;
        }
        h2, label, .result, .icon {
            color: #fff;
        }
        .icon { text-align: center; font-size: 48px; color: #fff; margin-bottom: 10px; }
        label { display: block; margin-top: 15px; }
        input[type=number] {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border-radius: 4px;
            border: 1px solid #444;
            background: #222;
            color: #fff;
        }
        input[type=number]::placeholder {
            color: #bbb;
        }
        button {
            margin-top: 20px;
            width: 100%;
            padding: 10px;
            background: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover { background: #0056b3; }
        .result { margin-top: 20px; text-align: center; font-size: 18px; color: #28a745; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon"><i class="fa-solid fa-book"></i></div>
        <h2>Student Performance Predictor</h2>
        <form method="post">
            <label>Attendance (%)</label>
            <input type="number" name="attendance" min="0" max="100" required>
            <label>Previous Marks</label>
            <input type="number" name="previous_marks" min="0" max="100" required>
            <label>Hours Studied (per week)</label>
            <input type="number" name="hours_studied" min="0" max="40" required>
            <label>Participation (1-5)</label>
            <input type="number" name="participation" min="1" max="5" required>
            <button type="submit">Predict</button>
        </form>
        {% if prediction is not none %}
        <div class="result">
            Predicted Final Score: <b>{{ prediction }}</b>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            attendance = float(request.form['attendance'])
            previous_marks = float(request.form['previous_marks'])
            hours_studied = float(request.form['hours_studied'])
            participation = float(request.form['participation'])
            input_df = pd.DataFrame({
                'Attendance': [attendance],
                'Previous_Marks': [previous_marks],
                'Hours_Studied': [hours_studied],
                'Participation': [participation]
            })
            pred = model.predict(input_df)[0]
            prediction = f"{pred:.2f}"
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template_string(TEMPLATE, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True) 