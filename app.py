from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("C:/Users/varsh/PycharmProjects/FlaskProject2/model_fit.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        price = float(request.form['Priceperweek'])
        population = int(request.form['Population'])
        income = float(request.form['Monthlyincome'])
        parking = float(request.form['Averageparkingpermonth'])

        # Make prediction
        features = np.array([[price, population, income, parking]])
        print("📦 Input to model:", features)

        prediction = model.predict(features)[0]
        print("✅ Prediction:", prediction)

        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        print("🔥 ERROR:", e)  # This shows the exact issue in terminal
        return render_template('result.html', prediction="Error: Invalid Input")

if __name__ == '__main__':
    app.run(debug=True)
